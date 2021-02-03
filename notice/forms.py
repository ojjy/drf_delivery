from django import forms
from .models import Notice, Image

class NoticeForm(forms.ModelForm):
    title = forms.CharField(max_length=128)
    content = forms.CharField(max_length=256, label="Item Description")
    class Meta:
        model = Notice
        fields = ('title', 'content')


class ImageForm(forms.ModelForm):
    img = forms.ImageField(label='Image')
    class Meta:
        model = Image
        fields = ('img',)
