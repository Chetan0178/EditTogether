# editor/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.editor_view, name='editor'),  # Renders editor.html
    path('api/document/', views.DocumentAPIView.as_view(), name='document_api'),  # API endpoint
]