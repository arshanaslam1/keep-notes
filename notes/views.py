from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from notes.models import Notes


class NoteListView(LoginRequiredMixin, ListView):
    model = Notes
    paginate_by = 8

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user).order_by('-created_on')


class NoteDetailView(DetailView, LoginRequiredMixin, UserPassesTestMixin):
    model = Notes

    def test_func(self):
        if self.request.user == self.object.user:
            return True
        return False


class NoteCreateView(CreateView, LoginRequiredMixin):
    model = Notes
    fields = "__all__"
    template_name_suffix = '_create_form'


class NoteUpdateView(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Notes
    fields = "__all__"
    template_name_suffix = '_update_form'

    def test_func(self):
        if self.request.user == self.object.user:
            return True
        return False


class NoteDeleteView(DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    model = Notes
    success_url = reverse_lazy('author_notes_list')

    def test_func(self):
        if self.request.user == self.object.user:
            return True
        return False

