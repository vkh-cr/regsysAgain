from django.forms import ModelForm
from .models import DetailRegistration


class RegistrationForm(ModelForm):
    class Meta:
        model = DetailRegistration
        exclude = ['status', 'price', 'date_created', 'var_symbol', 'reg_type', 'fri_breakfast', 'fri_lunch',
                   'fri_dinner', 'sat_breakfast', 'sat_lunch', 'sat_dinner', 'sun_breakfast', 'sun_lunch', 'fri_night',
                   'sat_night']
