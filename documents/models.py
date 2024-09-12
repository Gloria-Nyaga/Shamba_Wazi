from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

def validate_file_type(file):
    valid_mime_types = ['application/pdf', 'image/jpeg', 'image/png']
    mime_type = file.content_type

    if mime_type not in valid_mime_types:
        raise ValidationError('Unsupported file type. Only PDF, JPEG, and PNG files are allowed.')

class Document(models.Model):
    title = models.CharField(max_length=255, unique=True)
    file = models.FileField(upload_to='documents/', validators=[validate_file_type], blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='documents', null=True, blank=True)

    def __str__(self):
        return self.title
