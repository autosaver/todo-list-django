from django.shortcuts import render
from . import models
# Create your views here.
def baseview(request):
    return render(request, 'base.html')