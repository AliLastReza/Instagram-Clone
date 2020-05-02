from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from content.models import Post
from content.serializers import PostSerializer


class ContentView(generics.ListAPIView):
    authentication_classes = (JSONWebTokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    serializer_class = PostSerializer
    queryset = Post.objects.select_related('user', 'location').all()

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)