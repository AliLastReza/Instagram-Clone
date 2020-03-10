from django.contrib.auth import get_user_model
from django.db import transaction
from django.http import Http404
from django.shortcuts import redirect
from django.views import View

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
