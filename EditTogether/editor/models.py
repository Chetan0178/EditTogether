from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# editor/models.py
from django.db import models
from django.contrib.auth import get_user_model

class Document(models.Model):
    content = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Document updated at {self.updated_at}"
