from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('notes/', views.NoteListView.as_view(), name='author_notes_list'),
    path('add/', views.NoteCreateView.as_view(), name='note_create'),
    path('<int:pk>/update/', views.NoteUpdateView.as_view(), name='note_update'),
    path('<int:pk>/delete/', views.NoteDeleteView.as_view(), name='note_delete'),
    path('search/', views.SearchNoteView.as_view(), name='search_results'),
]
