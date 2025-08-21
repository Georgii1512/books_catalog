from django import forms
from . import models

class CatalogBookForm(forms.ModelForm):
    class Meta:
        model = models.CatalogBook
        fields = [
            'author', 'title', 'seria', 'pages_count', 'year', 'language', 'isbn'
        ]
