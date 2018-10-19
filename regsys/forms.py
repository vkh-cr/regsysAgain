from django.forms import ModelForm
from .models import DetailRegistration


class RegistrationForm(ModelForm):
    class Meta:
        model = DetailRegistration
        exclude = ['reg_id', 'status', 'price', 'date_created', 'var_symbol', 'reg_type']
