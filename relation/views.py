from django.contrib.auth import get_user_model
from django.http import Http404
from django.shortcuts import redirect
from django.views import View
from django.views.generic import ListView
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework import generics

from relation.serializers import RelationSerializer
from user.api.serializers import UserSerializer
from relation.models import Relation

User = get_user_model()


class FollowView(View):
    pattern_name = 'profile'

    def get_object(self):
        try:
            user = User.objects.get(username=self.kwargs.get('username'))
        except User.DoesNotExists:
            raise Http404
        return user

    def post(self, request, *args, **kwargs):
        target_user = self.get_object()
        if target_user == request.user:
            return redirect('/{}/'.format(target_user.username))
        qs = Relation.objects.filter(from_user=request.user, to_user=target_user)
        if qs.exists():
            qs.delete()
        else:
            Relation.objects.create(from_user=request.user, to_user=target_user)
        return redirect('/{}/'.format(target_user.username))


class FollowerListView(ListView):
    model = Relation
    template_name = "relation/FollowerList.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(to_user__username=self.kwargs["username"])
        return queryset


class FollowingListView(ListView):
    model = Relation
    template_name = "relation/FollowingList.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(from_user__username=self.kwargs["username"])
        return queryset


class FollowerListAPIView(generics.ListAPIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = RelationSerializer
    queryset = Relation.objects.select_related('to_user').all()

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(to_user=self.request.user)
