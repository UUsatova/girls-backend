from django.shortcuts import get_object_or_404

from api.models import ChatThread, ChatMessage, GirlProfile


def start_chat(user, girl_id):
    girl = get_object_or_404(GirlProfile, id=girl_id, is_active=True)
    thread, _created = ChatThread.objects.get_or_create(user=user, girl=girl)
    return thread


def send_message(user, thread_id, content):
    thread = get_object_or_404(ChatThread, id=thread_id, user=user)

    user_message = ChatMessage.objects.create(
        thread=thread,
        sender=ChatMessage.SENDER_USER,
        content=content,
    )

    ai_reply = (
        f"Hi {user.username}, I'm {thread.girl.name}. "
        f"I saw your message: \"{content[:200]}\". "
        "What would you like to talk about next?"
    )
    ai_message = ChatMessage.objects.create(
        thread=thread,
        sender=ChatMessage.SENDER_AI,
        content=ai_reply,
    )

    thread.save(update_fields=['updated_at'])
    return user_message, ai_message
