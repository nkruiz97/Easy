from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Element, Category

# Create your views here.

def index(request):
   ## elements = Element.objects.filter(type=2).all()

    search = request.GET.get('search') if request.GET.get('search') else '' 
    
    category_id = request.GET.get('category_id')
    category_id = int(category_id) if category_id else ''

    elements = Element.objects

    if search:
        elements = Element.objects.filter(title__contains=search)
    

    if category_id:
        elements = elements.filter(category_id=category_id)
    
    elements = elements.filter(type=2).all()

    categories = Category.objects.all()

    paginator = Paginator(elements,10)
    page_number = request.GET.get('page')
    return render(request, 'elements/index.html', {'elements':paginator.get_page(page_number), 'search':search, 'category_id':category_id, 'categories':categories})


def detail(request, pk):
    element = Element.objects.get(id=pk)
    return render(request, 'elements/detail.html',{'element':element})

def index0(request):
    return render(request, 'elements/index0.html')


def contacto(request):
    return render(request, 'elements/contacto.html')