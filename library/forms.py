from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title', 'author', 'isbn', 'description', 'category', 
            'image', 'availability', 'publication_date', 'pages', 
            'publisher', 'language'
        ]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Shkruaj titullin e librit'
            }),
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Shkruaj emrin e autorit'
            }),
            'isbn': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'p.sh. 9781234567890'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Shkruaj një përshkrim të shkurtër...'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control-file'
            }),
            'availability': forms.Select(attrs={
                'class': 'form-control'
            }),
            'publication_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'pages': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1'
            }),
            'publisher': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Shtëpia botuese'
            }),
            'language': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Gjuha e librit'
            }),
        }

class BookSearchForm(forms.Form):
    search = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Kërko sipas titullit, autorit ose ISBN...'
        })
    )
    category = forms.ChoiceField(
        choices=[('', 'Të gjitha kategoritë')] + Book.CATEGORY_CHOICES,
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )
    availability = forms.ChoiceField(
        choices=[('', 'Çdo disponueshmëri')] + Book.AVAILABILITY_CHOICES,
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )