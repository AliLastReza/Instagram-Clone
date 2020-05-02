from rest_framework import serializers

from activity.models import Comment, Like
from user.api.serializers import UserLightSerializer


class CommentSerializer(serializers.ModelSerializer):
    user = UserLightSerializer()

    class Meta:
        model = Comment
        fields = ('caption', 'user', 'created_time', 'reply_to', )


class LikeSerializer(serializers.ModelSerializer):
    user = UserLightSerializer()

    class Meta:
        model = Like
        fields = ('user', )
