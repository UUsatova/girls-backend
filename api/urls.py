from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from api.views import (
    RegisterView,
    MeView,
    GirlListView,
    GirlDetailView,
    ChatListView,
    ChatDetailView,
    StartChatView,
    MessageListView,
    SendMessageView,
)

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='auth-register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='auth-login'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='auth-refresh'),
    path('auth/me/', MeView.as_view(), name='auth-me'),

    path('girls/', GirlListView.as_view(), name='girls-list'),
    path('girls/<int:pk>/', GirlDetailView.as_view(), name='girls-detail'),

    path('chats/', ChatListView.as_view(), name='chats-list'),
    path('chats/<int:pk>/', ChatDetailView.as_view(), name='chats-detail'),
    path('chats/start/', StartChatView.as_view(), name='chats-start'),
    path('chats/<int:thread_id>/messages/', MessageListView.as_view(), name='chats-messages'),
    path('chats/<int:thread_id>/messages/send/', SendMessageView.as_view(), name='chats-messages-send'),
]
