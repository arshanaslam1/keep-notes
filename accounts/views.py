from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic as gen_views
from django.contrib.auth import views as auth_views

from .forms import AccountUpdateForm, AccountRegisterForm, AccountPasswordResetForm
from .models import User


class AccountUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, gen_views.UpdateView):
    model = User
    form_class = AccountUpdateForm
    template_name = 'accounts/user_view.html'
    success_message = 'You have update successfully'

    def form_valid(self, form):
        if self.request.user == form.instance.id:
            form.save()
        return super().form_valid(form)

    def test_func(self):
        object = self.get_object()
        if self.request.user.id == object.id:
            return True
        return False


class AccountRegisterView(SuccessMessageMixin, gen_views.CreateView):
    model = User
    form_class = AccountRegisterForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
    success_message = 'you have register account successfully'


class AccountLoginView(SuccessMessageMixin, auth_views.LoginView):
    model = User
    template_name = 'accounts/login.html'
    success_message = 'you have logged in successfully'


class AccountLogoutView(auth_views.LogoutView):
    template_name = 'accounts/logout.html'


class AccountPasswordResetView(auth_views.PasswordResetView):
    model = User
    form_class = AccountPasswordResetForm
    template_name = 'accounts/password_reset.html'


class AccountPasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html'


class AccountPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    model = User
    template_name = 'accounts/password_reset_confirm.html'


class AccountPasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'accounts/password_reset_complete.html'


class AccountPasswordChangeView(auth_views.PasswordChangeView):
    model = User
    template_name = 'accounts/password_change.html'


class AccountPasswordChangeDoneView(auth_views.PasswordChangeDoneView):
    template_name = 'accounts/password_change_done.html'
