from django import forms
from .models import Resources

class ResourceForm(forms.ModelForm):

    class Meta:
        model = Resources
        fields = ('title', 'author', 'url', 'description',)

