from django.urls import path 
from .views import articles_list, article_detail,article_create,article_change,article_delete

app_name = 'article'

urlpatterns = [
    path('', articles_list, name='list'),
    path('article/detail/<slug:slug>/', article_detail, name='detail'),
    path('article/create/', article_create, name='create'),
    path('article/change/<int:pk>/',article_change, name='change-form'),
    path('article/delete/<int:pk>/',article_delete, name='delete'),
]

