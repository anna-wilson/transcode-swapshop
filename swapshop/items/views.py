from django.shortcuts import render, redirect, reverse
from django.shortcuts import get_object_or_404
# from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse

from .models import Item, ItemImage, Comment, User
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
            return redirect(reverse('add_item'))
        else:
            messages.error(request, 'Failed to add item. Please ensure the form is valid.')
    else:
        item_form = ItemForm()

    template = 'items/add_item.html'
    context = {
        'item_form': item_form,
    }

    return render(request, template, context)


def item_detail(request, item_id):

    model = Item
    item = get_object_or_404(Item, pk=item_id)
    comment_form = CommentForm()
    comments = Comment.objects.filter(item=item)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST, request.FILES)
        if comment_form.is_valid():
            to_save = comment_form.save(commit=False)
            to_save.item = item
            to_save.save()
            messages.success(request, 'Comment successfully posted!')
            return redirect(reverse('index'))
        else:
            messages.error(request, 'Your comment was not sent. Please try again.')

    context = {
        'item': item,
        'comment_form': comment_form,
        'comments': comments
    }

    return render(request, 'items/item_detail.html', context)


def add_item_image(request, item_id):

    model = Item
    item = get_object_or_404(Item, item_id)
    item_image_form = ItemImageForm()
    images = ItemImage.objects.filter(item=item)

    if request.method == 'POST':
        # if request.user == Item.user:
        item_image_form = ItemImageForm(request.POST, request.FILES)
        if item_image_form.is_valid():
            item_image_form.save()
            messages.success(request, 'Successfully added item!')
            return redirect(reverse(''))
        else:
            messages.error(request, 'Failed to add image. Please ensure the form is valid.')

    context = {
        'item': item,
        'item_image_form': item_image_form,
        'images': images,
    }

    return render(request, 'items/item_detail.html', context)