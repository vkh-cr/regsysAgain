from django.shortcuts import render
from datetime import timedelta, datetime
from .models import DetailRegistration, Sleeping, RegStatus
from .forms import RegistrationForm

import .payment as p

def reg_test(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegistrationForm(request.POST)
        # check whether it's valid:

        if form.is_valid():
            form.save()

            last_user = DetailRegistration.objects.latest('pk')
            last_user.paymentNeed = (last_user.date_created + timedelta(days=14)).strftime('%d. %m. %Y')

            return render(request, 'thanks.html', {'reg': last_user})
        else:
            print(form.cleaned_data)
            form = RegistrationForm(initial=form.cleaned_data)
            return render(request, 'regsys/registrationForm.html', {'form': form, 'regtype': Sleeping.choices})
    # if a GET (or any other method) we'll create a blank form
    else:
        form = RegistrationForm()
        return render(request, 'regsys/registrationForm.html', {'form': form, 'regtype': Sleeping.choices})

def detailed_reg_form(request):
    # TODO copy from reg_test with DetailedRegistrationForm in mind

def pair_payments(request):
    # TODO parametrize by time period (eg last day)
    statement_json = p.download_statement_json()
    ps = p.json_to_payments(statement_json)
    ps.save()

    for pay in ps:
        p.process_payment(pay)

def cancel_timed_out_payments(request):
    # TODO check this condition is consistent with date in thank_you msg (reg. confirmation email)
    older_then = datetime.now() - timedelta(days=14)
    for reg in DetailRegistrations.objects.filter(date_created <= older_then):
        reg.status = RegStatus.EXPIRED
        reg.save()

def export_detailed_reg_excel(request):
    # TODO na to bude nejaka libka

