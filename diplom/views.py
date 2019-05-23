from django.shortcuts import render
from .models import Discipline

# Create your views here.


def dis_list(request):
    dis = Discipline.objects.all()
    return render(request, 'diplom/dis_list.html', {'dis':dis})