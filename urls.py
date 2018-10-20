from django.contrib import admin
from django.urls import path

from regsys import views


urlpatterns = [
    path('', views.reg_test),
    path('admin/', admin.site.urls),
    path('test/', views.reg_test),
]
