from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    name = request.GET.get('name')
    type = request.GET.get('type')
    humanoid = request.GET.get('humanoid')
    name_length = len(name)
    # humanoid = True
    if humanoid == '1':
        humanoid = "humanoid Да"
    elif humanoid == '0':
        humanoid = 'humanoid Нет'

    context = {'name': name,
               'type': type,
               'name_length': name_length,
               'humanoid': humanoid,
                              }
    return render(request, 'index.html', context=context)

