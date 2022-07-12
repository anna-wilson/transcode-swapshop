from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse

from .models import Item, ItemImage, Comment
from .forms import ItemForm, ItemImageForm, CommentForm


def index(request):
    itemlist = Item.objects.all()
    context = {'itemlist': itemlist}
    return render(request, 'items/index.html', context)


def add_item(request):

    if request.method == 'POST':
        item_form = ItemForm(request.POST, request.FILES)
        if item_form.is_valid():
            item_form.save()
            messages.success(request, 'Successfully added item!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add item. Please ensure the form is valid.')
    else:
        item_form = ItemForm()

    if request.method == 'POST':
        item_image_form = ItemImageForm(request.POST, request.FILES)
        if item_image_form.is_valid():
            item_image_form.save()
            messages.success(request, 'Successfully added item!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add item. Please ensure the form is valid.')
    else:
        item_image_form = ItemImageForm()
    
    

    template = 'items/add_item.html'
    context = {
        'item_form': item_form,
        'item_image_form': item_image_form,
    }

    return render(request, template, context)
