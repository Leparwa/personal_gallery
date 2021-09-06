from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ('image', 'image_name', 'image_description', 'image_location', 'image_category')