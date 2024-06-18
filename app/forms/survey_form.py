from datetime import datetime, timedelta

from django import forms
from ..models import Survey


class SurveyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # end_date 필드의 초기 값을 오늘 날짜에서 일주일 후로 설정
        initial_end_date = datetime.now() + timedelta(days=7)
        self.fields['end_date'].initial = initial_end_date.strftime('%Y-%m-%dT%H:%M')  # 날짜 형식에 맞게 포맷 지정

    def clean_thumbnail(self):
        thumbnail = self.cleaned_data['thumbnail']
        if not thumbnail:
            raise forms.ValidationError('썸네일은 필수 입력 항목입니다.')
        return thumbnail

    class Meta:
        model = Survey
        fields = ['title', 'description', 'thumbnail', 'is_searchable', 'end_date']
        widgets = {
            'end_date': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'thumbnail': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'is_searchable': forms.CheckboxInput(attrs={'class': 'form-check-input', 'checked': 'checked'}),
        }

