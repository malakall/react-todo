from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'название статьи'
            }),

            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'анонс статьи'
            }),

            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'время'
            }),

            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'текст статьи'
            })
        }
