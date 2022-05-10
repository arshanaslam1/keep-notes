from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from accounts.models import User
from notes.forms import NoteForm
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


# AJAX response
class JsonableResponseMixin:
    """
    Mixin to add JSON support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """

    def form_invalid(self, form):
        super().form_invalid(form)
        data = {
            'status': "False",
            'error': form.errors
        }
        # return JsonResponse(form.errors, status=400)
        return JsonResponse(data)

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        form.instance.user = self.request.user
        super().form_valid(form)
        data = {
            'status': "True",
            'message': self.success_message,
        }
        return JsonResponse(data, status=200)


class NoteCreateView(LoginRequiredMixin, JsonableResponseMixin, CreateView):
    model = Notes
    form_class = NoteForm
    success_message = 'You have add note successfully!'


class NoteUpdateView(UpdateView, LoginRequiredMixin, UserPassesTestMixin, JsonableResponseMixin):
    model = Notes
    form_class = NoteForm
    success_message = 'You have update note successfully!'

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


class SearchNoteView(ListView):
    template_name = 'notes/notes_list.html'
    paginate_by = 8

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user)
        query = self.request.GET.get('q')
        search_posts = user.notes.filter(
                Q(title__icontains=query)|
                Q(body__icontains=query)
            ).order_by('-created_on')
        return search_posts

