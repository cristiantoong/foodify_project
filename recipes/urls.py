from django.urls import path
from . import views

app_name = 'recipe_app'

urlpatterns = [
  path('', views.index, name='recipes'),
  path('<int:recipe_id>', views.recipe, name='recipe'),
  path('create/', views.recipe_create, name='create'),
  #path('userrecipes/', views.user_recipes, name='user_recipes'),
  path("search", views.search, name='search'),
]