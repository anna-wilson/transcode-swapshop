from django.contrib import admin

from .models import Item, ItemImage, Comment

admin.site.register(Item)
admin.site.register(ItemImage)
admin.site.register(Comment)
