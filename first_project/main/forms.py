from django.forms import ModelForm, TextInput, Textarea
from .models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'text']
        widgets = {
            'title': TextInput(attrs={
                'placeholder': 'Введіть заголовок'
            }),
            'text': Textarea(attrs={
                'placeholder': 'Введіть текст'
            })
        }
