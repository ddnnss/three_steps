from django.forms import ModelForm
from .models import *

class VacancyApplyForm(ModelForm):
    class Meta:
        model = VacancyApply
        fields = ('name',
                  'email',
                  'resume')
        exclude = ()


class ConsultationForm(ModelForm):
    class Meta:
        model = Consultation
        fields = ('category',
                    'town',
                    'name',
                    'phone',
                    'email',
                    'description',
                    'currency_type',
                    'price',
                    'street',
                    'street_number',
                    'floor',
                    'floor_total',
                    'rooms',
                    'square_total',
                    'square_kitchen',
                  )
        exclude = ()


