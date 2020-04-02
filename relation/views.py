from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.views import View
from django.views.generic import ListView
from django.shortcuts import redirect
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


class FollowerShow(ListView):
        model = Relation
        template_name = 'relation/followershow.html'

        def get_queryset(self):
            queryset = super().get_queryset()
            queryset = queryset.filter(to_user__username=self.kwargs['username'])
            return queryset


class FollowingShow(ListView):
    model = Relation
    template_name = 'relation/followingshow.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(from_user__username=self.kwargs['username'])
        return queryset
