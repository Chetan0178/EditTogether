# editor/consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
from rest_framework_simplejwt.tokens import AccessToken
from asgiref.sync import sync_to_async
from .models import Document, User
from urllib.parse import parse_qs
import logging
import json

logger = logging.getLogger(__name__)

class EditorConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = "editor_room"
        self.room_group_name = "editor_%s" % self.room_name

        # Extract token from query string
        query_string = self.scope['query_string'].decode()
        query_params = parse_qs(query_string)
        token = query_params.get('token', [''])[0]

        try:
            access_token = AccessToken(token)
            user_id = access_token['user_id']
            user = await sync_to_async(User.objects.get)(id=user_id)
            self.scope['user'] = user  # Set user in scope
           
            await self.channel_layer.group_add(self.room_group_name, self.channel_name)
            await self.accept()
            logger.info("WebSocket Connected!")
        except Exception as e:
            logger.info(f"Token validation error: {str(e)}")
            await self.close()
            logger.info("Invalid token")

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)
        logger.info("WebSocket Disconnected!")

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data.get("message")
        logger.info("message", message)
        # Save to database
        try:
            doc = await sync_to_async(Document.objects.latest)('updated_at')
            doc.content = message
            doc.updated_by = self.scope['user']
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