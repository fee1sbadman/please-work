from django.shortcuts import render, get_object_or_404
from .models import Discipline, Test

# Create your views here.


def dis_list(request):
    dis = Discipline.objects.all()
    return render(request, 'diplom/dis_list.html', {'dis':dis})


def dis_details(request, pk):
    dis = get_object_or_404(Discipline, pk = pk)
    return render(request, 'diplom/dis_details.html', {'dis': dis})