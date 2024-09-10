from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import os

class Document(models.Model):
    title = models.CharField(max_length=255, unique=True)
    file = models.FileField(upload_to='documents/', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)  
    # file_size = models.PositiveIntegerField( blank=True, null=True) 
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='documents', null=True, blank=True)
    is_draft = models.BooleanField(default=False) # This only applies to the drafted contract.
    editable_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='editable_documents', null=True, blank=True)  # Lawyer only
    land_owner_agreed = models.BooleanField(default=False)  # This is the agreement status of land owner
    land_seller_agreed = models.BooleanField(default=False)  # This is the agreement status of land seller
    
    
    def _str_ (self):
        return self.title

    # def save(self, *args, **kwargs):
    #     if self.file:
    #         self.file_size = self.file.size
    #     super().save(*args, **kwargs)
