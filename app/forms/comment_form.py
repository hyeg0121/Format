from django import forms
from ..models import Comment


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