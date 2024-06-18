from django import forms
from ..models import  Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'question_type']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'question_type': forms.Select(attrs={'class': 'form-control'}),
        }
