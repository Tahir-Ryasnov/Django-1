from django.shortcuts import render

from .models import Article


def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'
    object_list = Article.objects.all().order_by(ordering).prefetch_related('scopes')
    context = {'object_list': object_list}


    return render(request, template, context)
