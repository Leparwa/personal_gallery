from django import forms
from django.forms import widgets
from .models import Image

class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ('image', 'image_name', 'image_description', 'image_location', 'image_category')

        widgets={
            'image': forms.FileInput(attrs={'class':'form-control'}),
            'image_name': forms.TextInput(attrs={'class':'form-control'}),
            'image_description': forms.Textarea(attrs={'class':'form-control'}),
            'image_location': forms.Select(attrs={'class':'form-control'}),
            'image_category': forms.Select(attrs={'class':'form-control'}),
        }