from django.contrib import admin
from .models import Document

class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at','owner' ,)
    readonly_fields = ('uploaded_at', 'owner',) 
    search_fields = ('title',)  
    list_filter = ('uploaded_at',)  

admin.site.register(Document, DocumentAdmin)