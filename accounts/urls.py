from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/profile', views.ProfileView.as_view(), name='profile'),
    path('<int:pk>/update/', views.AccountUpdateView.as_view(), name='account_settings'),
    path('signup/', views.AccountRegisterView.as_view(), name='register'),
    path('login/', views.AccountLoginView.as_view(), name='login'),
    path('logout/', views.AccountLogoutView.as_view(), name='logout'),
    path('password-reset/', views.AccountPasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', views.AccountPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>',
         views.AccountPasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         views.AccountPasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
    path('password-change/',
         views.AccountPasswordChangeView.as_view(),
         name='password_change'),
    path('password-change/done/',
         views.AccountPasswordChangeDoneView.as_view(),
         name='password_change_done'),

]