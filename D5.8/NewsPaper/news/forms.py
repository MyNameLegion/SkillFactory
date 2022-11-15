from django import forms
from .models import Post
from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author',
                  'categoryType',
                  'category',
                  'title',
                  'text',
                  'rating',
                  ]

    def clean(self):
        clean_data = super().clean()
        text = clean_data.get('Текст')
        if text is not None and len(text) < 20:
            raise ValidationError({
                'Текст': 'Текст не может быть меньше 20 символов'
            })
        return clean_data
