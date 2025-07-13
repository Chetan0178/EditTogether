from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Document
from .serializers import DocumentSerializer
from django.shortcuts import render

class DocumentAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Return the latest document instance. 
        (You can extend this to fetch user-specific documents later.)
        """
        try:
            doc = Document.objects.latest('updated_at')
        except Document.DoesNotExist:
            return Response({"detail": "No document found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = DocumentSerializer(doc)
        return Response(serializer.data)
    
    def post(self, request):
        """
        Create a new document (only needed if you want API-based creation).
        """
        serializer = DocumentSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save(updated_by=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        try:
            doc = Document.objects.latest('updated_at')
        except Document.DoesNotExist:
            return Response({"detail": "No document found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = DocumentSerializer(doc, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(updated_by=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def editor_view(request):
    return render(request, 'editor/editor.html')
