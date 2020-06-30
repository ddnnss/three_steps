from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *



def articles(request):
    all_articles = Article.objects.filter(is_active=True).order_by('-created_at')
    pageTitle = ''
    pageDescription = ''
    articlePaginator = Paginator(all_articles, 1)
    try:
        allArticles = articlePaginator.get_page(request.GET.get('page'))
    except PageNotAnInteger:
        allArticles = articlePaginator.page(1)
    except EmptyPage:
        allArticles = articlePaginator.page(articlePaginator.num_pages)

    return render(request, 'article/articles.html', locals())


def article(request,article_name_slug):
    article = get_object_or_404(Article, name_slug=article_name_slug)
    pageTitle = article.name
    pageDescription = article.page_description
    return render(request, 'article/article.html', locals())
