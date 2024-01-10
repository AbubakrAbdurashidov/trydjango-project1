from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.db.models.signals import pre_save, post_save
from django.db.models import Q



class ArticlesQuerySet(models.QuerySet):
    def search(self, query=None):
        if query is None or query == "":
            return self.all()
        try:
            int(query)
        except:
            lookups = Q(title__incontains=query)
        else:
            lookups = Q(title__incontains=query) | Q(id=query)
        return self.filter(lookups)
    

    

class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(null=True, unique=True)
    content = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to="articles/",null=True,blank=True)
    modified_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)



    def __str__(self) -> str:
        return self.title


    @property
    def get_absolute_url(self):
        return reverse("article:detail", args=[self.id])


def article_pre_save(sender, instance, *arg, **kwargs):
    if instance.slug is None:
        instance.slug = slugify(instance.title)
    print("before save method")


def article_post_save(sender, instance, created, *arg, **kwargs):
    if created:
        instance.slug = slugify(instance.title) + "-" + str(instance.created_date.timestamp())
        instance.save()
        print("object is created")
    print('after save method')

pre_save.connect(article_pre_save, sender=Article)




