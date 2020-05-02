from rest_framework import serializers

from activity.serializers import CommentSerializer, LikeSerializer
from content.models import Post, PostMedia, PostTag, Tag
from user.api.serializers import UserLightSerializer


class MediaSerialize(serializers.ModelSerializer):
    class Meta:
        model = PostMedia
        fields = ('media_type', 'media_file',)


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('title', )


class PostTagSerializer(serializers.ModelSerializer):
    tag = TagSerializer()

    class Meta:
        model = PostTag
        fields = ('tag', )


class PostSerializer(serializers.ModelSerializer):
    user = UserLightSerializer()
    media = MediaSerialize(many=True)
    hashtags = PostTagSerializer(many=True)
    comments = CommentSerializer(many=True)
    likes = LikeSerializer(many=True)

    class Meta:
        model = Post
        fields = ('caption', 'user', 'media', 'hashtags', 'comments', 'likes', 'location')