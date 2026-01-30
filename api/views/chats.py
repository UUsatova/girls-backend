from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import ChatThread
from api.serializers import ChatThreadSerializer, ChatMessageSerializer
from api.services.chat_service import start_chat, send_message


class ChatListView(generics.ListAPIView):
    serializer_class = ChatThreadSerializer

    def get_queryset(self):
        return ChatThread.objects.filter(user=self.request.user).order_by('-updated_at')


class ChatDetailView(generics.RetrieveAPIView):
    serializer_class = ChatThreadSerializer

    def get_queryset(self):
        return ChatThread.objects.filter(user=self.request.user)


class StartChatView(APIView):
    def post(self, request):
        girl_id = request.data.get('girl_id')
        if not girl_id:
            return Response({'detail': 'girl_id is required'}, status=status.HTTP_400_BAD_REQUEST)
        thread = start_chat(request.user, girl_id)
        return Response(ChatThreadSerializer(thread).data, status=status.HTTP_201_CREATED)


class MessageListView(generics.ListAPIView):
    serializer_class = ChatMessageSerializer

    def get_queryset(self):
        thread = get_object_or_404(ChatThread, id=self.kwargs['thread_id'], user=self.request.user)
        return thread.messages.order_by('created_at')


class SendMessageView(APIView):
    def post(self, request, thread_id):
        content = (request.data.get('content') or '').strip()
        if not content:
            return Response({'detail': 'content is required'}, status=status.HTTP_400_BAD_REQUEST)

        user_message, ai_message = send_message(request.user, thread_id, content)

        return Response(
            {
                'user_message': ChatMessageSerializer(user_message).data,
                'ai_message': ChatMessageSerializer(ai_message).data,
            },
            status=status.HTTP_201_CREATED,
        )
