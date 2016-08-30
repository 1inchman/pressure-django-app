from django.shortcuts import render
from pressure.models import Measurment, User
from pressure.forms import MeasurmentForm


# def index(request):
#     return render(request, 'pressure/index.html')


def about(request):
    context_dict = {'name': "Ax-er"}
    return render(request, 'pressure/about.html', context=context_dict)


def index(request):
    if request.method == 'POST':
        form = MeasurmentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return render(request, 'pressure/index.html', {'form': form})
    else:
        form = MeasurmentForm()

    return render(request, 'pressure/index.html', {'form': form})
