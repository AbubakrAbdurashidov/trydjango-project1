from django.contrib import admin

# Register your models here.

from .models import Article



class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id" , "title", 'modified_date', "created_date", "slug")
    # fields = ('title','content','modified_date', 'created_date')
    readonly_fields = ("created_date",'modified_date', 'slug')
    list_filter = ('created_date',)
    date_hierarchy = ('created_date')
    list_display_links = ('id','title',)
    search_fields = ('title',)
    list_per_page = 2 
    prepopulated_fields = {"slug":("title",)}

admin.site.register(Article, ArticleAdmin)