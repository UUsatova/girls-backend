from rest_framework import serializers

from api.models import GirlProfile, Tag, GirlPhoto


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class GirlPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GirlPhoto
        fields = ['id', 'image_url', 'sort_order']


class GirlProfileSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    photos = GirlPhotoSerializer(many=True, read_only=True)

    class Meta:
        model = GirlProfile
        fields = ['id', 'name', 'age', 'bio', 'story', 'image_url', 'tags', 'is_new', 'photos']
