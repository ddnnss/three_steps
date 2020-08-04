import json
from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from ads.models import *
from .models import *
from .forms import *
from ads.forms import *


def index(request):
    pageTitle = 'Агентство недвижимости в Москве и области (Королев, Мытищи, Балашиха, Фрязино, Щелково, Пушкино) '
    pageDescription = 'Купить / Продать / Снять / Сдать недвижимость. Большая база квартир и домов. Работаем быстро и качественно. Агентство недвижимости "ТРИ СТУПЕНИ". Звоните 8 (495) 760-20-58'
    allCategories = Category.objects.all()
    allSubCategories = SubCategory.objects.all()
    towns = Town.objects.all()
    allMetros = Metro.objects.all()
    is_index_page=True


    return render(request, 'pages/index.html', locals())

def consultation(request):
    pageTitle = 'Помощь в продаже и покупке недвижимости. Консультации и помощь в выборе и оформление документов.  '
    pageDescription = 'Бесплатная консультация специалистов по недвижимости. Агентство недвижимости "ТРИ СТУПЕНИ" Звоните 8 (495) 760-20-58'

    towns = Town.objects.all()
    categories = Category.objects.all()
    consult_form = ConsultationForm()
    return render(request, 'pages/consultation.html', locals())

def add_consultation(request):
    if request.POST:
        if not request.POST.get('age') or not request.POST.get('comment') != '':
            form = ConsultationForm(request.POST)
            if form.is_valid():
                form.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    towns = Town.objects.all()
def credit_calculator(request):
    pageTitle = 'Рассчитать стоимость кредита под недвижимость. Онлайн калькулятор'
    pageDescription = 'Расчет процентной ставки и окупаемости недвижимости. Онлайн калькулятор стоимости кредита. '
    return render(request, 'pages/credit-calculator.html', locals())

def credit_help(request):
    pageTitle = 'Помощь в оформление кредита на квартиры и дома. Консультация специалиста в сфере недвижимости.'
    pageDescription = 'Подготовка и помощь в подаче документов на кредит под недвижимость. Агентство недвижимости "ТРИ СТУПЕНИ" Звоните 8 (495) 760-20-58'
    towns = Town.objects.all()
    categories = Category.objects.all()
    consult_form = ConsultationForm()
    return render(request, 'pages/credit-help.html', locals())

def jobs(request):
    if request.POST:
        form = VacancyApplyForm(request.POST, request.FILES)
        if form.is_valid():
            vacancy = Vacancy.objects.get(id=request.POST.get('v_id'))
            new_apply = form.save(commit=False)
            new_apply.vacancy = vacancy
            new_apply.save()
            applyJob = vacancy.id
            jobs = Vacancy.objects.filter(is_active=True)
            form = VacancyApplyForm()
            return render(request, 'pages/jobs.html', locals())
    pageTitle = 'Работа в агентстве недвижимости "ТРИ СТУПЕНИ"'
    pageDescription = 'Вакансии для специалистов в сфере недвижимости. Работа для риэлтора. Агентство недвижимости "ТРИ СТУПЕНИ"'
    towns = Town.objects.all()
    jobs = Vacancy.objects.filter(is_active=True)
    form = VacancyApplyForm()

    return render(request, 'pages/jobs.html', locals())

def owners(request):
    pageTitle = 'Помощь в продаже недвижимости в Москве и области. Предварительная оценка и помощь в подготовке недвижимости на продажу.'
    pageDescription = 'Работаем по всей Москве и  в таких городах как: Королев, Мытищи, Балашиха, Фрязино, Щелково, Пушкино. Агентство недвижимости "ТРИ СТУПЕНИ" Звоните 8 (495) 760-20-58'
    towns = Town.objects.all()
    categories = Category.objects.all()
    consult_form = ConsultationForm()
    return render(request, 'pages/owners.html', locals())

def partners(request):
    pageTitle = 'Наши партнеры'
    pageDescription = 'Агентство недвижимости "ТРИ СТУПЕНИ" Звоните 8 (495) 760-20-58'
    towns = Town.objects.all()
    return render(request, 'pages/partners.html', locals())

def privatization(request):
    pageTitle = 'Помощь в оформление документов - Приватизация плюсы и минусы.'
    pageDescription = 'Оформить перепланировку квартиры. Помощь в оформление документов на квартиру (приватизировать квартиру) Агентство недвижимости "ТРИ СТУПЕНИ". Звоните 8 (495) 760-20-58'
    towns = Town.objects.all()
    return render(request, 'pages/privatization.html', locals())

def contacts(request):
    pageTitle = 'Наши контакты. '
    pageDescription = 'Агентство недвижимости "ТРИ СТУПЕНИ" Звоните 8 (495) 760-20-58'
    towns = Town.objects.all()
    return render(request, 'pages/contacts.html', locals())

def contact(request):
    pageTitle = 'Наши контакты. '
    pageDescription = 'Агентство недвижимости "ТРИ СТУПЕНИ" Звоните 8 (495) 760-20-58'
    towns = Town.objects.all()
    return render(request, 'pages/contact.html', locals())

def sell(request):
    if request.POST:
        print(request.POST)
        if not request.POST.get('age') or not request.POST.get('comment') !='':
            form = SellForm(request.POST)
            new_ads = None
            if form.is_valid():
                new_ads = form.save()
                if new_ads:
                    for f in request.FILES.getlist('images'):
                        AdsImage.objects.create(ads_id=new_ads.id, image=f).save()
            else:
                pass
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    towns = Town.objects.all()
    sellForm = SellForm()
    subcategories = SubCategory.objects.all()
    return render(request, 'pages/sell.html', locals())

def estimate(request):
    towns = Town.objects.all()
    sellForm = SellForm()
    categories = Category.objects.all()
    return render(request, 'pages/estimate.html', locals())

def robots(request):
    robotsTxt = f"User-agent: *\nDisallow: /admin/\nHost: https://www.3stypeni.ru//\nSitemap: https://www.3stypeni.ru/sitemap.xml"
    return HttpResponse(robotsTxt, content_type="text/plain")

def customhandler404(request, exception, template_name='404.html'):
    return render(request, 'pages/404.html', None,None,status=404)

def new_callback(request):
    request_unicode = request.body.decode('utf-8')
    request_body = json.loads(request_unicode)

    ad = Ads.objects.get(number=request_body['number'])
    Callback.objects.create(name=request_body['name'],
                            phone=request_body['phone'],
                            time=request_body['time'],
                            ads=ad
                            )
    return JsonResponse({'result':'ok'}, safe=False)

def get_info(request):
    request_unicode = request.body.decode('utf-8')
    request_body = json.loads(request_unicode)

    if request_body['action'] == 'getSubcats':
        cat = Category.objects.get(name_slug=request_body['value'])
        subcats = []
        for subcat in cat.subcategory_set.all():
            subcats.append({
                'id':subcat.id,
                'type':subcat.name
            })

        return JsonResponse(subcats, safe=False)
    if request_body['action'] == 'getMetros':
        town = Town.objects.get(name_slug=request_body['value'])
        metros = []
        metros.append({'id':'0', 'type':'Метро любое'})
        for metro in town.metros.all():

            metros.append({
                'id':metro.id,
                'type':metro.name
            })

        return JsonResponse(metros, safe=False)

    if request_body['action'] == 'getSubcatInfo':
        subcategory = SubCategory.objects.get(id=request_body['value'])
        subcatInfo = []
        subcatInfo.append(
                {'show_building_type': subcategory.show_building_type,
                'show_square_kitchen': subcategory.show_square_kitchen,
                'show_square_land': subcategory.show_square_land,
                'show_floors': subcategory.show_floors,
                'show_rooms': subcategory.show_rooms,
                'show_house_type': subcategory.show_house_type
                 })

        return JsonResponse(subcatInfo, safe=False)

def searchIt(request):
    request_unicode = request.body.decode('utf-8')
    request_body = json.loads(request_unicode)

    result=[]
    filterAds= False
    allAds = Ads.objects.filter(is_publish=True,
                                action_type=request_body['action_type'],
                                subcategory_id=request_body['subcat'],
                                town__name_slug=request_body['town'],
                                currency_type=request_body['currency']).order_by(request_body['order'])

    if request_body['start_price'] == '':
        start_price = 0
    else:
        start_price = request_body['start_price']

    allAds = allAds.filter(Q(price__gte=start_price) & Q(price__lte=request_body['end_price']))

    if request_body['square_total_from'] !='' and request_body['square_total_to'] !='':
        allAds = allAds.filter(Q(square_total__gte=request_body['square_total_from']) & Q(square_total__lte=request_body['square_total_to']))
    elif request_body['square_total_from'] !='' and request_body['square_total_to'] =='':
        allAds = allAds.filter(square_total__gte=request_body['square_total_from'])
    elif request_body['square_total_from'] =='' and request_body['square_total_to'] !='':
        allAds = allAds.filter(square_total__lte=request_body['square_total_to'])

    if request_body['square_kitchen_from'] !='' and request_body['square_kitchen_to'] !='':
        allAds = allAds.filter(Q(square_kitchen__gte=request_body['square_kitchen_from']) & Q(square_kitchen__lte=request_body['square_kitchen_to']))
    elif request_body['square_kitchen_from'] !='' and request_body['square_kitchen_to'] =='':
        allAds = allAds.filter(square_kitchen__gte=request_body['square_kitchen_from'])
    elif request_body['square_kitchen_from'] =='' and request_body['square_kitchen_to'] !='':
        allAds = allAds.filter(square_kitchen__lte=request_body['square_kitchen_to'])

    if request_body['rooms'] !='':

        allAds = allAds.filter(rooms__exact=request_body['rooms'])

    if request_body['floor'] != '':

        allAds = allAds.filter(floor__exact=request_body['floor'])

    if request_body['floors'] != '':

        allAds = allAds.filter(floor_total__exact=request_body['floors'])



    if request_body['building_type'] == 'old':
        allAds = allAds.filter(is_new_building=False)
    if request_body['building_type'] == 'new':
        allAds = allAds.filter(is_new_building=True)

    if request_body['house_type'] != '':

        allAds = allAds.filter(house_type__exact=request_body['house_type'])

    if request_body['metro'] != '0':
        allAds = allAds.filter(metro__exact=request_body['metro'])






    articlePaginator = Paginator(allAds, 10)
    try:
        allAdsPaginator = articlePaginator.get_page(request_body['page'])
    except PageNotAnInteger:
        allAdsPaginator = articlePaginator.page(1)
    except EmptyPage:
        allAdsPaginator = articlePaginator.page(articlePaginator.num_pages)

    for ad in allAdsPaginator:
        images=[]
        for img in ad.get_images():
            images.append(img.image_main.url)
        result.append({
                        'number':ad.number,
                        'price':ad.price,
                        'rooms':ad.get_rooms_display(),
                        'square':f'{ad.square_total}/{ad.square_living}/{ad.square_kitchen} - м2',
                        'floors': f'Этаж {ad.floor}/{ad.floor_total}',
                        'address':f'г.{ad.town} ,{ad.street}, д. {ad.street_number}',
                        'date':f'{ad.created_at.strftime("%d/%m/%Y")}',
                        'images':images,
                        'currency':ad.get_currency()

                    })





    return JsonResponse({'result':result,'pages':articlePaginator.num_pages,'page':int(request_body['page'])}, safe=False)