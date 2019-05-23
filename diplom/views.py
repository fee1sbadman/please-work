from django.shortcuts import render

# Create your views here.


def dis_list(request):
    return render(request, 'diplom/dis_list.html', {})