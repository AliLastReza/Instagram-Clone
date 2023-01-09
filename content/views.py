from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from content.models import Post
from content.serializers import PostListSerializer


class PostListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostListSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)
