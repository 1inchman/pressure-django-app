from django.shortcuts import render


def index(request):
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake"}
    return render(request, 'pressure/index.html', context=context_dict)


def about(request):
    context_dict = {'name': "Ax-er"}
    return render(request, 'pressure/about.html', context=context_dict)
