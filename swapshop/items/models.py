from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=200)
    available = models.BooleanField(default=False)

class ItemImage(models.Model):
    item = models.ForeignKey(
        'Item',
        on_delete = models.CASCADE
    )
    desc = models.CharField(max_length=200)

class Comment(models.Model):
    item = models.ForeignKey(
        'Item',
        on_delete = models.CASCADE
    )
    text = models.TextField()
