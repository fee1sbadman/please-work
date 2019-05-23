from django.urls import path
from . import views


urlpatterns = [
    path('', views.dis_list, name = 'discipline_list'),
    path('post/<int:pk>/', views.dis_details, name = 'dis_details'),
]
