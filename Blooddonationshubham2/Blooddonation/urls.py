from django.urls import path

from . import views

urlpatterns = [
    
    path('', views.home, name='home'),
    path ('eligiblity/',views.eligiblity,name='eligiblity')
    
]