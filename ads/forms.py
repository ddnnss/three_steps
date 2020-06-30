from django.forms import ModelForm
from .models import *



class SellForm(ModelForm):
    class Meta:
        model = Ads
        fields = ('category',
                  'name',
                  'street',
                  'house_type',
                  'rooms',
                  'floor',
                  'floor_total',
                  'square_total',
                  'square_kitchen',
                  'description',
                  'price',
                  'currency_type',
                  'contact_name',
                  'contact_phone',
                  'contact_email',
                  'ads_type',
                  'action_type',
                  )
        exclude = ()


