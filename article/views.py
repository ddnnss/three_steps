from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *



def articles(request):
    all_articles = Article.objects.filter(domain=request.domain, is_active=True).order_by('-created_at')
    page_title = request.domain.articles_page_title
    page_description = request.domain.articles_page_description
    page_keywords = request.domain.articles_page_keywords

    articlePaginator = Paginator(all_articles, settings.ARTICLES_PER_PAGE)
    try:
        allArticles = articlePaginator.get_page(request.GET.get('page'))
    except PageNotAnInteger:
        allArticles = articlePaginator.page(1)
    except EmptyPage:
        allArticles = articlePaginator.page(articlePaginator.num_pages)

    return render(request, 'page/articles.html', locals())


def article(request,article_name_slug):
    article = get_object_or_404(Article, name_slug=article_name_slug)
    advantages = Advantage.objects.filter(domain=request.domain)
    # Разбиваем название статьи на части, делитель пробел
    # search_patterns = article.name.split(' ')
    # similar = []
    similar_ids = article.similar.split(',')
    page_h1 = request.domain.articles_page_h1
    try:
        similar_articles = Article.objects.filter(id__in=similar_ids)
    except:
        similar_articles = None


    if article.page_title:
        page_title = article.page_title
    else:
        page_title = article.name
    page_description = article.page_description
    page_keywords = article.page_keywords

    # for pattern in search_patterns:
    #     # если слово более 3 символов ищем похожие статьи с этим словом в названии
    #     if len(pattern) > 3:
    #         temp_search = Article.objects.filter(domain=request.domain, name__contains=pattern).exclude(id=article.id)
    #         # если что-то найдено, сохраняем результат поиска за исключением текущей статьи
    #         if temp_search:
    #             similar.append(temp_search)

    # Если к статье прикреплены услуги, то происходит подмена ключевого слова %%SERVICES%%
    if article.services.all():
        temp_services = ''
        for service in article.services.all():
            temp_services = temp_services + f'<div class="services-row">' \
                                            f'<div class="services-col services-col__1">' \
                                            f'<p><a href="#">{service.name}</a></p></div>'\
                                            f'<div class="services-col services-col__2">'\
                                            f'<p>{service.time}</p>'\
                                            f'</div>'\
                                            f'<div class="services-col services-col__3">'\
                                            f'<b> {service.price} Р</b>'\
                                            f'</div>'\
                                            f'</div>'
        services = f'<h2 class="section-title">Мои услуги</h2>' \
                   f'<div class="services-table">{temp_services}</div>'
        articleText = article.text.replace('%%SERVICES%%',services)
    else:
        articleText = article.text.replace('%%SERVICES%%','')
    return render(request, 'page/article.html', locals())
