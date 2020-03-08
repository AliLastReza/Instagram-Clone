from django.contrib.auth import authenticate, login, get_user_model
from django.views.generic import FormView, UpdateView

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
