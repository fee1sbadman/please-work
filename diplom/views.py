from django.shortcuts import render, get_object_or_404
from .models import Discipline, Test
from django.views import generic
from django.core.paginator import Paginator

# Create your views here.


def dis_list(request):
      dis = Discipline.objects.all()
      return render(request, 'diplom/dis_list.html', {'dis':dis})



def dis_detail(request, pk):
      dis = get_object_or_404(Discipline, pk = pk)
      return render(request, 'diplom/dis_detail.html', {'dis':dis})