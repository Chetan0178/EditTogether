# editor/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from rest_framework_simplejwt.tokens import AccessToken
from .models import Document
from django.contrib.auth import get_user_model
from urllib.parse import parse_qs
from asgiref.sync import sync_to_async

class EditorConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = "editor_room"
        self.room_group_name = "editor_%s" % self.room_name

        # Extract token from query string
        query_string = self.scope['query_string'].decode()
        query_params = parse_qs(query_string)
        token = query_params.get('token', [''])[0]

        try:
            AccessToken(token)  # Validate token
            await self.channel_layer.group_add(self.room_group_name, self.channel_name)
            await self.accept()
            print("WebSocket Connected!")
        except Exception as e:
            print(f"Token validation error: {str(e)}")
            await self.close()
            print("Invalid token")

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)
        print("WebSocket Disconnected!")

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data.get("message")
        # Save to database
        try:
            doc = await sync_to_async(Document.objects.latest)('updated_at')
            doc.content = message
            await sync_to_async(doc.save)()
        except Document.DoesNotExist:
            await sync_to_async(Document.objects.create)(content=message, updated_by=self.scope['user'])
        # Broadcast
        await self.channel_layer.group_send(
            self.room_group_name,
            {"type": "editor_message", "message": message}
        )

    async def editor_message(self, event):
        message = event["message"]
        await self.send(text_data=json.dumps({"message": message}))