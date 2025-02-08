from django.contrib import admin
from .models import Upload, Metadata

@admin.register(Upload)
class UploadAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'file', 'uploaded_at')
    search_fields = ('user__username',)
    list_filter = ('uploaded_at',)

@admin.register(Metadata)
class MetadataAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'url', 'title', 'created_at')
    search_fields = ('url', 'title', 'user__username')
    list_filter = ('created_at',)
