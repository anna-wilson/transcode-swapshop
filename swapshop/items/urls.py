from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_item/', views.add_item, name='add_item'),
    # path('add_item/', views.add_item_image, name='add_item_image'),
]