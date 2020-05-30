from rest_framework import serializers

from activity.serializers import CommentSerializer, LikeSerializer
from content.models import Post, PostMedia, PostTag, Tag, TaggedUser
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


class TaggedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaggedUser
        fields = ('user',)


class PostCreateSerializer(serializers.ModelSerializer):
    tagged_users = TaggedUserSerializer(many=True)

    class Meta:
        model = Post
        fields = ('caption', 'location', 'tagged_users')

    def create(self, validated_data):
        tagged_users = validated_data.pop('tagged_users')
        post_instance = super().create(validated_data)
        for user in tagged_users:
            TaggedUser.objects.create(user=user.get('user'),
                                      post=post_instance)
        return post_instance