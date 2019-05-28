from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    path('', views.dis_list, name = 'dis_list'),
    path('discipline/<int:pk>/', views.dis_detail, name = 'dis_detail'),
    ]
