from django.core.management.base import BaseCommand

from api.models import GirlProfile, Tag


SEED_GIRLS = [
    {
        'name': 'Isabella',
        'age': 24,
        'bio': 'Art student by day, digital dreamer by night. I love deep conversations about philosophy and spontaneous adventures.',
        'story': 'Isabella grew up in a coastal town where sunsets felt like a ritual. She sketches people in cafes and keeps a folder of unfinished poems. If you bring curiosity, she will bring warmth and a surprising sense of humor.',
        'image_url': 'https://images.unsplash.com/photo-1616002411355-49593fd89721?q=80&w=800&auto=format&fit=crop',
        'photos': [
            'https://images.unsplash.com/photo-1524504388940-b1c1722653e1?q=80&w=800&auto=format&fit=crop',
            'https://images.unsplash.com/photo-1494790108377-be9c29b29330?q=80&w=800&auto=format&fit=crop',
        ],
        'tags': ['Artistic', 'Playful'],
        'is_new': True,
    },
    {
        'name': 'Marcus',
        'age': 29,
        'bio': 'Fitness enthusiast and personal chef. Looking for someone to share healthy recipes and workout tips with.',
        'story': 'Marcus is an early riser who believes the best conversations happen after a good workout. He keeps a journal of recipes, and his kitchen is always stocked with fresh herbs and citrus.',
        'image_url': 'https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?q=80&w=800&auto=format&fit=crop',
        'photos': [
            'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?q=80&w=800&auto=format&fit=crop',
            'https://images.unsplash.com/photo-1517841905240-472988babdf9?q=80&w=800&auto=format&fit=crop',
        ],
        'tags': ['Fitness', 'Cooking'],
        'is_new': False,
    },
    {
        'name': 'Sophia',
        'age': 26,
        'bio': "Tech entrepreneur building the future. When I'm not coding, I'm exploring virtual worlds.",
        'story': 'Sophia built her first game at 15 and never stopped. She loves sharing new ideas and exploring cities late at night with a podcast on.',
        'image_url': 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?q=80&w=800&auto=format&fit=crop',
        'photos': [
            'https://images.unsplash.com/photo-1531746020798-e6953c6e8e04?q=80&w=800&auto=format&fit=crop',
            'https://images.unsplash.com/photo-1529626455594-4ff0802cfb7e?q=80&w=800&auto=format&fit=crop',
        ],
        'tags': ['Smart', 'Ambitious'],
        'is_new': True,
    },
    {
        'name': 'Aria',
        'age': 22,
        'bio': "Music producer and DJ. Let's make some noise and create beautiful harmonies together.",
        'story': 'Aria spends her nights in a neon-lit studio mixing tracks. She collects vinyls and can lose hours talking about the stories behind them.',
        'image_url': 'https://images.unsplash.com/photo-1529626455594-4ff0802cfb7e?q=80&w=800&auto=format&fit=crop',
        'photos': [
            'https://images.unsplash.com/photo-1488426862026-3ee34a7d66df?q=80&w=800&auto=format&fit=crop',
            'https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?q=80&w=800&auto=format&fit=crop',
        ],
        'tags': ['Music', 'Creative'],
        'is_new': False,
    },
    {
        'name': 'Lucas',
        'age': 31,
        'bio': 'Architect with a passion for sustainable design. I appreciate structure, beauty, and intelligent design.',
        'story': 'Lucas travels to sketch buildings and keeps a notebook of ideas for future spaces. He loves conversations about form, light, and hidden details.',
        'image_url': 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?q=80&w=800&auto=format&fit=crop',
        'photos': [
            'https://images.unsplash.com/photo-1534528741775-53994a69daeb?q=80&w=800&auto=format&fit=crop',
            'https://images.unsplash.com/photo-1494790108377-be9c29b29330?q=80&w=800&auto=format&fit=crop',
        ],
        'tags': ['Design', 'Intellectual'],
        'is_new': False,
    },
    {
        'name': 'Eva',
        'age': 25,
        'bio': 'Fashion designer obsessed with textures and colors. I see the world as a canvas waiting to be painted.',
        'story': 'Eva has a moodboard for everything. She loves thrift stores, late-night studio sessions, and conversations about what style means to you.',
        'image_url': 'https://images.unsplash.com/photo-1488426862026-3ee34a7d66df?q=80&w=800&auto=format&fit=crop',
        'photos': [
            'https://images.unsplash.com/photo-1524504388940-b1c1722653e1?q=80&w=800&auto=format&fit=crop',
            'https://images.unsplash.com/photo-1517841905240-472988babdf9?q=80&w=800&auto=format&fit=crop',
        ],
        'tags': ['Fashion', 'Style'],
        'is_new': True,
    },
]


class Command(BaseCommand):
    help = 'Seed the database with demo girl profiles.'

    def handle(self, *args, **options):
        for payload in SEED_GIRLS:
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
        self.stdout.write(self.style.SUCCESS('Seeded girl profiles.'))
