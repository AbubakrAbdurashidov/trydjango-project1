from django.shortcuts import render
from article.models import Article
from .form import ArticleForm
from django.shortcuts import reverse
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

# Create your views here.


def articles_list(request):
    query = request.GET.get('q')
    articles = Article.objects.all()
    
    if query:
        articles = Article.objects.filter(title__icontains=query)
    context = {
        'object_list':articles,
    }
    return render(request, 'article/index.html',context)


def article_detail(request, slug):
    articles = Article.objects.get(slug=slug)
    context = {
        'object':articles,
    }
    return render(request, 'article/detail.html',context)


def article_create(request):


    context = {
        'created': False,
    }
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        obj = Article.objects.create(title=title, content=content)
        context['created'] = True
        context['object'] = obj
    return render(request, 'article/create.html', context)


def article_create_(request,):
    
    context = {

    }


    return render(request, 'article/create.html', context)


def article_change(request, pk):
    obj = Article.objects.get(id=pk)
    form = ArticleForm(instance=obj)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            reverse_url = reverse('article:change-form', kwargs={"pk": obj.id})
            return redirect(reverse_url)
    context = {
            'form':form,
            'object':obj,
    }
    return render(request, 'article/edit.html', context)

def article_delete(request, pk):
    obj = get_object_or_404(Article, id=pk)
    if request.method == "POST":
        obj.delete()
        reverse_url = reverse('article:list')
        return redirect(reverse_url)
    context = {
        'object':obj,
    }
    return render(request, 'article/delete.html',context)