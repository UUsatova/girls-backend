from rest_framework import generics, permissions

from api.models import GirlProfile
from api.serializers import GirlProfileSerializer
from api.services.girls_service import list_girls


class GirlListView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = GirlProfileSerializer

    def get_queryset(self):
        search = self.request.query_params.get('search')
        tag = self.request.query_params.get('tag')
        is_new = self.request.query_params.get('is_new')
        return list_girls(search=search, tag=tag, is_new=is_new)


class GirlDetailView(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = GirlProfileSerializer
    queryset = GirlProfile.objects.filter(is_active=True).prefetch_related('tags', 'photos')
