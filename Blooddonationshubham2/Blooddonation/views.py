from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
import logging
from decimal import Decimal
from  django . conf  import  settings
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def home(request):
    return render(request,'Blooddonation/home.html')

def index(request):
    return render(request,'Blooddonation/index.html')
def eligiblity(request):
    return render(request,'Blooddonation/eligiblity.html')

