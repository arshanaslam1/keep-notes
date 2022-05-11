from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/profile', views.ProfileView.as_view(), name='profile'),
    path('<int:pk>/update/', views.AccountUpdateView.as_view(), name='update_profile'),
]