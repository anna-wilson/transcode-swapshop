from django.shortcuts import render

# Create your views here.

from .models import Item


def index(request):

    itemlist = Item.objects.all()
    context = {'itemlist': itemlist}
    return render(request, 'items/index.html', context)
