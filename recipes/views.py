from django.shortcuts import get_object_or_404, render, redirect

from .models import Recipe
from django.contrib.auth.decorators import login_required
from . import forms
#from django.contrib.auth.models import User
from accounts.models import UserProfile

def index(request):
  recipes = Recipe.objects.order_by('-list_date').filter(is_published=True)

  context = {
    'recipes': recipes
  }

  return render(request, 'recipes/recipes.html', context)




def recipe(request, recipe_id):
  recipe = get_object_or_404(Recipe, pk=recipe_id)
  context = {
    'recipe':recipe
  }
  return render(request, 'recipes/recipe.html', context)




@login_required(login_url="/accounts/login/")
def recipe_create(request):
  if request.method == 'POST':
    form = forms.CreateRecipe(request.POST, request.FILES)
    if form.is_valid():
          
      #save recipe to db
      instance = form.save(commit=False)
      instance.author = request.user
      instance.save()
      return redirect('accounts:profile')   
  else:      
    form = forms.CreateRecipe()

  context = {
    'form': form
  }
  return render(request, 'recipes/recipe_create.html', context)

def search(request):
  #return render(request, 'recipes/search.html')
  queryset_list = Recipe.objects.all().order_by('-list_date')

  # Keywords
  if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    if keywords:
        queryset_list = queryset_list.filter(title__icontains=keywords)

  context = {
      'recipes': queryset_list,
      'values': request.GET  #perserving form input
  }

  return render(request, 'recipes/search.html', context)


 
def all_photos(request):
  main_photos = Recipe.objects.filter(is_published=True)

  context = {
    'main_photos': main_photos
  }

  return render(request, 'recipes/recipe.html', context)

