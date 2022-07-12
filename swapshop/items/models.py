from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    name = models.CharField(max_length=200)
    available = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class ItemImage(models.Model):
    img = models.ImageField(null=True)
    item = models.ForeignKey(
        'Item',
        on_delete = models.CASCADE
    )
    desc = models.CharField(max_length=200)

    def __str__(self):
        return str(self.img)

class Comment(models.Model):
    item = models.ForeignKey(
        'Item',
        on_delete = models.CASCADE
    )
    text = models.TextField()


