from django.urls import path
from . import views

app_name ='pages'

urlpatterns = [
  path("", views.index, name='recipes'),
  path("about/", views.about, name='about'),
]