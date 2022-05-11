from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic as gen_views
from .forms import AccountUpdateForm
from .models import User


class ProfileView(LoginRequiredMixin, UserPassesTestMixin, gen_views.DetailView):
    model = User
    template_name = 'accounts/profile.html'
    context_object_name = 'object'

    def test_func(self):
        object = self.get_object()
        if self.request.user.id == object.id:
            return True
        return False


class AccountUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, gen_views.UpdateView):
    model = User
    form_class = AccountUpdateForm
    template_name = 'accounts/profile_settings.html'
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


