from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from ads.models import *
from .models import *
from .forms import *

def index(request):
    pageTitle = 'Недвижимость в Королеве | Агентство недвижимости Королев - 3 Ступени'
    pageDescription = ''
    allCategories = Category.objects.all()
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
    return render(request, 'pages/sell.html', locals())

def robots(request):
    robotsTxt = f"User-agent: *\nDisallow: /admin/\nHost: https://ugscash.ru/\nSitemap: https://ugscash.ru/sitemap.xml"
    return HttpResponse(robotsTxt, content_type="text/plain")

def customhandler404(request, exception, template_name='404.html'):
    return render(request, 'pages/404.html', None,None,status=404)