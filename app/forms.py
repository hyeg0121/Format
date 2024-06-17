from datetime import datetime, timedelta

from django import forms
from .models import Survey, Question, Comment


class SurveyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # end_date 필드의 초기 값을 오늘 날짜에서 일주일 후로 설정
        initial_end_date = datetime.now() + timedelta(days=7)
        self.fields['end_date'].initial = initial_end_date.strftime('%Y-%m-%dT%H:%M')  # 날짜 형식에 맞게 포맷 지정

    class Meta:
        model = Survey
        fields = ['title', 'description', 'thumbnail_path', 'is_searchable', 'end_date']
        widgets = {
            'end_date': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'thumbnail_path': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'is_searchable': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'question_type']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'question_type': forms.Select(attrs={'class': 'form-control'}),
        }


class SurveyResponseForm(forms.Form):
    pass  # Dynamic fields are added in the view based on the survey questions


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['contents']
        widgets = {
            'contents': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'contents': '댓글을 입력하세요',
        }