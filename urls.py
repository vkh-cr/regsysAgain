from django.contrib import admin
from django.urls import path

from regsys import views


urlpatterns = [
    path('', views.see_reg_form, name='seeForm'),
    path('registration/', views.see_reg_form, name='seeForm'),
    path('admin/', admin.site.urls),
    path('test/', views.reg_test),
]
