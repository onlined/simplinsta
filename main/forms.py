from django import forms

from .models import Tag

class TagForm(forms.ModelForm):
    
    name = forms.CharField(label='Search')
    
    class Meta:
        model = Tag
        fields = ['name']
