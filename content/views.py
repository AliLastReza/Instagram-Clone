from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from content.models import Post
from content.serializers import PostSerializer, PostCreateSerializer


class ContentView(generics.ListAPIView):
    # authentication_classes = (JSONWebTokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    serializer_class = PostSerializer
    queryset = Post.objects.select_related('user', 'location').all()
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ('location',)
    search_fields = ('caption',)

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)


class PostCreateView(generics.CreateAPIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = PostCreateSerializer
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)