from django.shortcuts import render
from . import models


# Create your views here.
def index(request):
    dests = app.objects.all()
    return render(request , 'index.html', {'dests':dests})