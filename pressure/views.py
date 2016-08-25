from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake"}
    return render(request, 'pressure/index.html', context=context_dict)


def about(request):
    link = '<a href=/pressure/>click</a>'
    return HttpResponse(link)
