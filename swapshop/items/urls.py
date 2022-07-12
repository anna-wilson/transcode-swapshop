from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_item/', views.add_item, name='add_item'),
    path('add_item_image/<item_id>', views.add_item_image, name='add_item_image'),
    path('item_detail/<item_id>', views.item_detail, name='item_detail'),
]