from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'elements/index.html')


def detail(request, pk):
    print(pk)
    return render(request, 'elements/detail.html')