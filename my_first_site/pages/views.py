from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    name = request.GET.get('name')
    type = request.GET.get('type')
    humanoid = True
    name_length = len(name)
    context = {'name': name,
               'type': type,
               'name_length': name_length
                              }
    return render(request, 'index.html', context=context)

