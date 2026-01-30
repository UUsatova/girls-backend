from django.conf import settings
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class GirlProfile(models.Model):
    name = models.CharField(max_length=120)
    age = models.PositiveIntegerField()
    bio = models.TextField()
    story = models.TextField(blank=True, default='')
    image_url = models.URLField(max_length=500)
    tags = models.ManyToManyField(Tag, related_name='girls', blank=True)
    is_new = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class GirlPhoto(models.Model):
    girl = models.ForeignKey(GirlProfile, on_delete=models.CASCADE, related_name='photos')
    image_url = models.URLField(max_length=500)
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['sort_order', 'id']

    def __str__(self):
        return f"{self.girl_id}:{self.sort_order}"


class ChatThread(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='chat_threads')
    girl = models.ForeignKey(GirlProfile, on_delete=models.CASCADE, related_name='chat_threads')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'girl')

    def __str__(self):
        return f"{self.user_id}-{self.girl_id}"


class ChatMessage(models.Model):
    SENDER_USER = 'user'
    SENDER_AI = 'ai'
    SENDER_CHOICES = [
        (SENDER_USER, 'User'),
        (SENDER_AI, 'AI'),
    ]

    thread = models.ForeignKey(ChatThread, on_delete=models.CASCADE, related_name='messages')
    sender = models.CharField(max_length=10, choices=SENDER_CHOICES)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.thread_id}:{self.sender}" 
