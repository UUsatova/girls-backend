from api.views.auth import RegisterView, MeView
from api.views.girls import GirlListView, GirlDetailView
from api.views.chats import ChatListView, ChatDetailView, StartChatView, MessageListView, SendMessageView

__all__ = [
    'RegisterView',
    'MeView',
    'GirlListView',
    'GirlDetailView',
    'ChatListView',
    'ChatDetailView',
    'StartChatView',
    'MessageListView',
    'SendMessageView',
]
