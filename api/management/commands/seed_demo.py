from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.utils import timezone

from api.models import GirlProfile, Tag, ChatThread, ChatMessage

User = get_user_model()

DEMO_USERS = [
    {
        'username': 'demo',
        'email': 'demo@example.com',
        'password': 'DemoPass123!',
    },
    {
        'username': 'alex',
        'email': 'alex@example.com',
        'password': 'AlexPass123!',
    },
]

EXTRA_GIRLS = [
    {
        'name': 'Luna',
        'age': 23,
        'bio': 'Late-night astronomer and ambient playlist curator. I believe in slow conversations and stargazing.',
        'story': 'Luna watches the city skyline and keeps a notebook of constellations. She loves soft lighting and dreamy playlists.',
        'image_url': 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?q=80&w=800&auto=format&fit=crop',
        'photos': [
            'https://images.unsplash.com/photo-1529626455594-4ff0802cfb7e?q=80&w=800&auto=format&fit=crop',
            'https://images.unsplash.com/photo-1494790108377-be9c29b29330?q=80&w=800&auto=format&fit=crop',
        ],
        'tags': ['Calm', 'Curious'],
        'is_new': False,
    },
    {
        'name': 'Mira',
        'age': 27,
        'bio': 'Bookworm and barista. Let me guess your favorite genre and make you a perfect latte.',
        'story': 'Mira keeps a shelf of well-loved paperbacks and likes to annotate in the margins. She believes coffee is a love language.',
        'image_url': 'https://images.unsplash.com/photo-1524504388940-b1c1722653e1?q=80&w=800&auto=format&fit=crop',
        'photos': [
            'https://images.unsplash.com/photo-1534528741775-53994a69daeb?q=80&w=800&auto=format&fit=crop',
            'https://images.unsplash.com/photo-1531746020798-e6953c6e8e04?q=80&w=800&auto=format&fit=crop',
        ],
        'tags': ['Cozy', 'Thoughtful'],
        'is_new': True,
    },
    {
        'name': 'Jade',
        'age': 25,
        'bio': 'UX designer with a soft spot for neon lights and rainy nights. Tell me your latest obsession.',
        'story': 'Jade collects design postcards and spends weekends exploring galleries. She always notices the little things.',
        'image_url': 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?q=80&w=800&auto=format&fit=crop',
        'photos': [
            'https://images.unsplash.com/photo-1517841905240-472988babdf9?q=80&w=800&auto=format&fit=crop',
            'https://images.unsplash.com/photo-1488426862026-3ee34a7d66df?q=80&w=800&auto=format&fit=crop',
        ],
        'tags': ['Design', 'Modern'],
        'is_new': True,
    },
    {
        'name': 'Nova',
        'age': 28,
        'bio': 'Fitness coach and weekend hiker. Let’s trade playlists and trail stories.',
        'story': 'Nova is happiest on a trail with a thermos of tea. She likes steady conversations and honest goals.',
        'image_url': 'https://images.unsplash.com/photo-1517841905240-472988babdf9?q=80&w=800&auto=format&fit=crop',
        'photos': [
            'https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?q=80&w=800&auto=format&fit=crop',
            'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?q=80&w=800&auto=format&fit=crop',
        ],
        'tags': ['Active', 'Supportive'],
        'is_new': False,
    },
]

CHAT_SNIPPETS = [
    (
        'user',
        'Hey! What are you up to tonight?'
    ),
    (
        'ai',
        "I just finished a sketch and I’m about to make tea. Want to keep me company?"
    ),
    (
        'user',
        'Absolutely. Tell me about your latest project.'
    ),
    (
        'ai',
        'It’s a moody cityscape with neon reflections. I’ll send you a glimpse if you promise feedback.'
    ),
]


class Command(BaseCommand):
    help = 'Seed demo users, girl profiles, and chat messages.'

    def handle(self, *args, **options):
        self._seed_users()
        self._seed_girls()
        self._seed_chats()
        self.stdout.write(self.style.SUCCESS('Seeded demo data.'))

    def _seed_users(self):
        for payload in DEMO_USERS:
            user, created = User.objects.get_or_create(
                username=payload['username'],
                defaults={'email': payload['email']},
            )
            if created:
                user.set_password(payload['password'])
                user.save(update_fields=['password'])

    def _seed_girls(self):
        for payload in EXTRA_GIRLS:
            tags = payload.pop('tags')
            photos = payload.pop('photos', [])
            profile, _created = GirlProfile.objects.update_or_create(
                name=payload['name'],
                defaults=payload,
            )
            profile.tags.clear()
            for tag_name in tags:
                tag, _ = Tag.objects.get_or_create(name=tag_name)
                profile.tags.add(tag)
            profile.photos.all().delete()
            for index, photo_url in enumerate(photos):
                profile.photos.create(image_url=photo_url, sort_order=index)

    def _seed_chats(self):
        demo_user = User.objects.filter(username='demo').first()
        if not demo_user:
            return
        girls = list(GirlProfile.objects.filter(is_active=True)[:3])
        for girl in girls:
            thread, _ = ChatThread.objects.get_or_create(user=demo_user, girl=girl)
            if thread.messages.exists():
                continue
            for sender, content in CHAT_SNIPPETS:
                ChatMessage.objects.create(
                    thread=thread,
                    sender=sender,
                    content=content,
                    created_at=timezone.now(),
                )
