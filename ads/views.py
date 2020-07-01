from django.shortcuts import render, get_object_or_404
from .models import Ads

def show_ads(request,ads_number):
    ads = get_object_or_404(Ads, number=ads_number)

    return render(request, 'pages/ads.html', locals())