from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader, Context
from datetime import datetime

from .models import Ads

def show_ads(request,ads_number):
    ads = get_object_or_404(Ads, number=ads_number)

    return render(request, 'pages/ads.html', locals())

def feed(request,):
    template_vars = {}
    template_vars['ads'] = Ads.objects.filter(is_publish=True, is_in_ya_feed=True)
    template_vars['created'] = datetime.now().strftime('%Y-%m-%dT%H:%M:%S+03:00')

    t = loader.get_template('pages/feed.xml')
    c = template_vars
    return HttpResponse(t.render(c),content_type='text/xml')




