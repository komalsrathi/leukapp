from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def lists_page(request):
    return HttpResponse('<html><title>TO-DO lists</title></html>')
