from django.db.models import Q

from api.models import GirlProfile


def list_girls(search=None, tag=None, is_new=None):
    queryset = GirlProfile.objects.filter(is_active=True).prefetch_related('tags', 'photos')

    if search:
        queryset = queryset.filter(Q(name__icontains=search) | Q(bio__icontains=search))
    if tag:
        queryset = queryset.filter(tags__name__iexact=tag)
    if is_new in {'true', 'false'}:
        queryset = queryset.filter(is_new=(is_new == 'true'))

    return queryset.distinct().order_by('name')
