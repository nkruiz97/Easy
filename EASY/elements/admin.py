from django.contrib import admin
from .models import Element, Category, Type, Carousel

# Register your models here.
admin.site.register(Element)
admin.site.register(Category)
admin.site.register(Type)
admin.site.register(Carousel)