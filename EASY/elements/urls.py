from django.urls import path
from . import views

app_name = 'elements'

urlpatterns = [
    path('', views.index0, name='index0'),
    path('<int:pk>', views.detail, name='detail'),
    path('index/', views.index, name='index'),
    path('contacto/', views.contacto, name='contacto'),
] 