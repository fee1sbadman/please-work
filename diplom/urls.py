from django.urls import path
from . import views


urlpatterns = [
    path('', views.dis_list, name = 'discipline_list'),
]
