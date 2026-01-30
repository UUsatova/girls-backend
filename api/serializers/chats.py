from rest_framework import serializers

from api.models import ChatThread, ChatMessage
from api.serializers.girls import GirlProfileSerializer


class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = ['id', 'thread', 'sender', 'content', 'created_at']
        read_only_fields = ['id', 'thread', 'sender', 'created_at']


class ChatThreadSerializer(serializers.ModelSerializer):
    girl = GirlProfileSerializer(read_only=True)
    last_message = serializers.SerializerMethodField()

    class Meta:
        model = ChatThread
        fields = ['id', 'girl', 'created_at', 'updated_at', 'last_message']

    def get_last_message(self, obj):
        message = obj.messages.order_by('-created_at').first()
        if not message:
            return None
        return {
            'id': message.id,
            'sender': message.sender,
            'content': message.content,
            'created_at': message.created_at,
        }
