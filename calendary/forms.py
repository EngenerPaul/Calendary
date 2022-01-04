from django import forms
from django.db.models import fields
from .models import Lesson


class FormLesson(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['pupil_name', 'pupil_surname', 'pupils_father', 
            'theme', 'note', 'salary', 'time', 'date']
        widgets = {
            'pupil_name':forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': '...',
            }),
            'pupil_surname':forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': '(необязательно)',
            }),
            'pupils_father':forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': '(необязательно)',
            }),
            'theme':forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': '...',
            }),
            'note':forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 5,
                'placeholder': '(необязательно)',
            }),
            'salary':forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': '...',
            }),
            'time':forms.TimeInput(attrs={
                'class': 'form-control', 
                'placeholder': '00:00:00',
            }),
            'date.title':forms.DateInput(attrs={
                'class': 'form-control', 
                'placeholder': '...',
            }),
        }
