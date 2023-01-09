from rest_framework import serializers

from content.models import Post, PostMedia
from location.serializers import LocationSerializer
from user.api.serializers import UserLightSerializer


class PostMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostMedia
        fields = ('media_type', 'media_file')


class PostListSerializer(serializers.ModelSerializer):
    user = UserLightSerializer()
    location = LocationSerializer()
    media = PostMediaSerializer(many=True)

    class Meta:
        model = Post
        # TODO: Add post_tag and tagged_user to the list API
        # TODO: Likes and Comments count
        fields = ('id', 'caption', 'user', 'location', 'media')
