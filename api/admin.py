from django.contrib import admin

from .models import GirlProfile, Tag, ChatThread, ChatMessage, GirlPhoto


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(GirlProfile)
class GirlProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'is_new', 'is_active']
    search_fields = ['name', 'bio']
    list_filter = ['is_new', 'is_active']


@admin.register(GirlPhoto)
class GirlPhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'girl', 'sort_order']
    search_fields = ['girl__name']


@admin.register(ChatThread)
class ChatThreadAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'girl', 'created_at']
    search_fields = ['user__username', 'girl__name']


@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'thread', 'sender', 'created_at']
    search_fields = ['content']
    list_filter = ['sender']
