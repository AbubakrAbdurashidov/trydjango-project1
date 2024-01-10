from django.contrib import admin
from .models import (
    Tag,
    Recipe,
    Ingredient,
)

# admin.site.register(Tag)
# admin.site.register(Recipe)
# admin.site.register(Ingredient)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "title",)
    search_fields = ("title",)
    list_display_links = ('id', 'title',)


class IngredientAdminTabularInline(admin.TabularInline):
    model = Ingredient
    extra = 0


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientAdminTabularInline]
    list_display = ("id", "title", "author", "created_date", 'slug')
    search_fields = ("title", "author__username",)
    list_filter = ("created_date", 'author',)
    autocomplete_fields = ("author",)
    list_display_links = ('id', 'title',)
    filter_horizontal = ('tags',)
    date_hierarchy = 'created_date'
    readonly_fields = ('slug', 'created_date',)


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ("id", "recipe", "title", "quantity", "unit", "is_active")
    search_fields = ("recipe__title", "title",)
    list_filter = ("is_active", 'unit',)
    autocomplete_fields = ("recipe",)

