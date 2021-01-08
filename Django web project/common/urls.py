from common.views import *
from django.urls import path

urlpatterns = [
    path('', landing_page, name='index'),
]
