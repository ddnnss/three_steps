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
    pageTitle = 'Недвижимость в Королеве | Агентство недвижимости Королев - 3 Ступени'
    pageDescription = ''
    allCategories = Category.objects.all()
    allSubCategories = SubCategory.objects.all()
    allTowns = Town.objects.all()
    allMetros = Metro.objects.all()


    return render(request, 'pages/index.html', locals())

def consultation(request):
    towns = Town.objects.all()
    categories = Category.objects.all()
    consult_form = ConsultationForm()
    return render(request, 'pages/consultation.html', locals())

def add_consultation(request):
    if request.POST:
        form = ConsultationForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
def credit_calculator(request):
    return render(request, 'pages/credit-calculator.html', locals())

def credit_help(request):
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
    jobs = Vacancy.objects.filter(is_active=True)
    form = VacancyApplyForm()

    return render(request, 'pages/jobs.html', locals())

def owners(request):
    towns = Town.objects.all()
    categories = Category.objects.all()
    consult_form = ConsultationForm()
    return render(request, 'pages/owners.html', locals())

def partners(request):
    return render(request, 'pages/partners.html', locals())

def privatization(request):
    return render(request, 'pages/privatization.html', locals())

def contacts(request):
    return render(request, 'pages/contacts.html', locals())

def contact(request):
    return render(request, 'pages/contact.html', locals())

def sell(request):
    if request.POST:
        print(request.POST)
        form = SellForm(request.POST)
        new_ads = None
        if form.is_valid():
            new_ads = form.save()
            if new_ads:
                for f in request.FILES.getlist('images'):
                    AdsImage.objects.create(ads_id=new_ads.id, image=f).save()
        else:
            print(form.errors)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    sellForm = SellForm()
    subcategories = SubCategory.objects.all()
    return render(request, 'pages/sell.html', locals())

def estimate(request):
    sellForm = SellForm()
    categories = Category.objects.all()
    return render(request, 'pages/estimate.html', locals())

def robots(request):
    robotsTxt = f"User-agent: *\nDisallow: /admin/\nHost: https://ugscash.ru/\nSitemap: https://ugscash.ru/sitemap.xml"
    return HttpResponse(robotsTxt, content_type="text/plain")

def customhandler404(request, exception, template_name='404.html'):
    return render(request, 'pages/404.html', None,None,status=404)



def get_info(request):
    request_unicode = request.body.decode('utf-8')
    request_body = json.loads(request_unicode)
    print(request_body)
    if request_body['action'] == 'getSubcats':
        cat = Category.objects.get(name_slug=request_body['value'])
        subcats = []
        for subcat in cat.subcategory_set.all():
            subcats.append({
                'id':subcat.id,
                'type':subcat.name
            })
        print(subcats)
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
        print(metros)
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
        print(subcatInfo)
        return JsonResponse(subcatInfo, safe=False)

def searchIt(request):
    request_unicode = request.body.decode('utf-8')
    request_body = json.loads(request_unicode)
    print(request_body)
    result=[]
    filterAds= False
    allAds = Ads.objects.filter(is_publish=True,
                                action_type=request_body['action_type'],
                                subcategory_id=request_body['subcat'],
                                town__name_slug=request_body['town'],
                                currency_type=request_body['currency']).order_by(request_body['order'])
    print(allAds)
    allAds = allAds.filter(Q(price__gte=request_body['start_price']) & Q(price__lte=request_body['end_price']))

    if request_body['rooms'] !='':
        print('rooms',request_body['rooms'])
        allAds = allAds.filter(rooms__exact=request_body['rooms'])

    if request_body['floor'] != '':
        print('floor', request_body['floor'])
        allAds = allAds.filter(floor__exact=request_body['floor'])

    if request_body['floors'] != '':
        print('floors', request_body['floors'])
        allAds = allAds.filter(floor_total__exact=request_body['floors'])


    print('building_type', request_body['building_type'])
    if request_body['building_type'] == 'old':
        allAds = allAds.filter(is_new_building=False)
    if request_body['building_type'] == 'new':
        allAds = allAds.filter(is_new_building=True)

    if request_body['house_type'] != '':
        print('house_type', request_body['house_type'])
        allAds = allAds.filter(house_type__exact=request_body['house_type'])

    print(allAds)

    articlePaginator = Paginator(allAds, 10)
    try:
        allAdsPaginator = articlePaginator.get_page(request_body['page'])
    except PageNotAnInteger:
        allAdsPaginator = articlePaginator.page(1)
    except EmptyPage:
        allAdsPaginator = articlePaginator.page(articlePaginator.num_pages)
    print('articlePaginator.num_pages',articlePaginator.num_pages)
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