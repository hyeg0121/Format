from django.db import models
from django.conf import settings


class Question(models.Model):
    SUBJECTIVE = 'SUBJECTIVE'
    SINGLE_CHOICE = 'SINGLE_CHOICE'
    QUESTION_TYPES = [
        (SUBJECTIVE, '주관식'),
        (SINGLE_CHOICE, '단일 선택')
    ]

    survey = models.ForeignKey('Survey', on_delete=models.CASCADE, related_name='questions', verbose_name='설문조사')
    title = models.CharField(max_length=100, verbose_name='문항 제목')
    question_type = models.CharField(max_length=15, choices=QUESTION_TYPES, verbose_name='문항 타입')
    options = models.JSONField(null=True, blank=True, verbose_name='선택지 (객관식)')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='생성 날짜')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='마지막 수정 날짜')

    def __str__(self):
        return f"Survey ID: {self.survey_id}, Title: {self.title}, Question Type: {self.get_question_type_display()}"

    class Meta:
        verbose_name = '설문 문항'
        verbose_name_plural = '설문 문항'