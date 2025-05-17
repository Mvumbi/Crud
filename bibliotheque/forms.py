# forms.py
from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['author', 'title', 'content']
        widgets = {
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Nom de l’auteur"
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Titre du livre"
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': "Résumé ou description du livre"
            }),
        }
        