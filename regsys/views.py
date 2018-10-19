from django.shortcuts import render
from datetime import timedelta
from .models import DetailRegistration, Sleeping
from .forms import RegistrationForm


def see_reg_form(req):
    form = RegistrationForm()
    return render(req, 'regsys/registrationForm.html', {'form': form})


def process_application(req):
    simpleReg = RegistrationForm(req.POST)
    detailedReg = DetailRegistration(simpleReg)
    detailedReg.save()
    # send email


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

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RegistrationForm()
    return render(request, 'regsys/registrationForm.html', {'form': form, 'regtype': Sleeping.choices})
