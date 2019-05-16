from django.shortcuts import render

from django.http import HttpResponse

from recipes.models import Recipe


def index(request):
  recipes = Recipe.objects.order_by('-list_date').filter(is_published=True)

  context = {
      'recipes': recipes
  }

  return render(request, 'recipes/recipes.html', context)


def about(request):
  return render(request, 'pages/about.html')


