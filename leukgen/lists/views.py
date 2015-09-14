from django.shortcuts import render

# Create your views here.


def lists_page(request):
    return render(request, 'lists_home.html')
