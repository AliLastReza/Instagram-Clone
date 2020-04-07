from django.contrib.auth import login, get_user_model
from django.views.generic import FormView, UpdateView, DetailView, ListView

from relation.models import Relation
from user.forms import RegistrationForm, LoginForm


User = get_user_model()


class RegisterView(FormView):
    form_class = RegistrationForm
    template_name = 'user/register.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'user/login.html'
    success_url = '/'

    def form_valid(self, form):
        login(self.request, form.cleaned_data['user'])
        return super().form_valid(form)


class ProfileUpdateView(UpdateView):
    model = User
    fields = ('username', 'avatar', 'bio', 'website')
    template_name = 'user/profile_update.html'
    success_url = '/'

    def get_object(self, queryset=None):
        return self.request.user


class ProfileDetailView(DetailView):
    model = User
    slug_url_kwarg = 'username'
    slug_field = 'username'
    template_name = 'user/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts_count'] = user.posts.count()
        context['followers_count'] = user.followers.count()
        context['followings_count'] = user.followings.count()
        context['is_following'] = Relation.objects.filter(from_user=self.request.user, to_user=user).exists()
        return context


class FollowerDetail(ListView):
    template_name = 'user/follower_detail.html'

    def get_object(self):
        target_user = User.objects.filter(username=self.kwargs.get('username')).first()
        return target_user

    def get_queryset(self):
        user = self.get_object()
        queryset = user.followers.all().values_list('from_user__username', flat=True)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        target_user = self.get_object()
        context['target_user'] = target_user.username
        return super().get_context_data(**context)


class FollowingDetail(ListView):
    template_name = 'user/following-detail.html'

    def get_object(self):
        target_user = User.objects.filter(username=self.kwargs.get('username')).first()
        return target_user

    def get_queryset(self):
        user = self.get_object()
        queryset = user.followings.all().values_list('to_user__username', flat=True)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        target_user = self.get_object()
        context['target_user'] = target_user.username
        return super().get_context_data(**context)
