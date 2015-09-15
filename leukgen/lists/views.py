from django.shortcuts import redirect, render
from django.core.urlresolvers import reverse

from .models import Item

# Create your views here.


def home_page(request):
    if request.method == 'POST':
        new_item_text = request.POST['item_text']
        Item.objects.create(text=new_item_text)
        return redirect('/lists/the-only/')
    return render(request, 'lists/list_home.html')


def view_list(request):
    items = Item.objects.all()
    return render(request, 'lists/list_list.html', {'items': items})
