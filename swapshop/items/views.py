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


def item_page(request):

     if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added item!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add item. Please ensure the form is valid.')
    else:
        form = ItemForm()

    template = 'items/add_item.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
