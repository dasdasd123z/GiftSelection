from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index/index.html')

def select(request):
    return render(request, 'index/select.html')
def selecthttp(request):
    return obr(request, obr.py(input_teg))
