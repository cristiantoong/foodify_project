from django.contrib import admin

from .models import Recipe



# admin.site.register(User)


class RecipeAdmin(admin.ModelAdmin):
  list_display = ('id', 'title')
  list_display_links = ('id', 'title')
  #list_editable = ('is_published',)
  search_fields = ('title', 'body')
  list_per_page = 25

admin.site.register(Recipe, RecipeAdmin)