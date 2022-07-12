from django import forms
from .models import Item, ItemImage, Comment


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ItemImageForm(forms.ModelForm):

    class Meta:
        model = ItemImage
        fields = '__all__'
    
    image = forms.ImageField(label='Image', required=True)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
