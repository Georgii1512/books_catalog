from django import forms
from . import models


class CatalogBookForm(forms.ModelForm):
    class Meta:
        model = models.CatalogBook
        fields = [
            'author',
            'title',
            'seria',
            'pages_count',
            'year',
            'language',
            'isbn'
        ]

    def __init__(self, *args, **kwargs):
        """
        Replaces the default field values with the labels.
        :param args:
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.initial = None
            field.widget.attrs['placeholder'] = field.label


class CatalogBookSearchForm(forms.Form):
    isbn = forms.CharField(label='ISBN', max_length=13, required=True)
