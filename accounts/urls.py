from django.urls import path, include, re_path
from django.conf.urls import url
from . import views
from django.contrib.auth.views import (
  PasswordResetView, 
  PasswordResetDoneView, 
  PasswordResetConfirmView,
  PasswordResetCompleteView
)

app_name = 'accounts'

urlpatterns = [
  path('signup/', views.signup_view, name='signup'),
  path('login/', views.login_view, name='login'),
  path('logout/', views.logout_view, name='logout'),
  path('profile', views.view_profile, name='profile'),
  path('profile/', views.view_profile, name='view_profile'),
  path('profile/edit', views.edit_profile, name='edit_profile'),
  path('change-password', views.change_password, name='change_password'),
  path('reset-password', PasswordResetView.as_view(), name='reset_password'),
  path('reset-password/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
  url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
  path('reset-password/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),

  
  #path('profile/', views.user_recipes, name='user_recipes'),
  #path("recipes/", include('recipes.urls')),
  
]
