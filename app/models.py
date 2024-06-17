from django.db import models
from django.conf import settings


class Survey(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='작성자')
    title = models.CharField(max_length=100, verbose_name='설문조사 제목')
    description = models.TextField(verbose_name='설문조사 설명')
    thumbnail_path = models.ImageField(upload_to='thumbnails/', null=True, blank=True, verbose_name='썸네일 이미지 경로')
    is_searchable = models.BooleanField(default=False, verbose_name='검색 가능 여부')
    end_date = models.DateTimeField(verbose_name='설문조사 마감 날짜')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='생성 날짜')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='마지막 수정 날짜')

    def __str__(self):
        return f'Title: {self.title}, Description: {self.description}'

    class Meta:
        verbose_name = '설문조사'
        verbose_name_plural = '설문조사'


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


class Response(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='응답자')
    survey = models.ForeignKey('app.Survey', on_delete=models.CASCADE, related_name='answers', verbose_name='설문조사')
    responses = models.JSONField(default=list, verbose_name='응답')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='생성 날짜')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='마지막 수정 날짜')

    def __str__(self):
        return f'User ID: {self.user.id}, Survey ID: {self.survey.id}, Responses: {len(self.responses)}'

    class Meta:
        verbose_name = '응답'
        verbose_name_plural = '응답'


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='작성자')
    survey = models.ForeignKey('app.Survey', on_delete=models.CASCADE, related_name='comments', verbose_name='설문조사')
    contents = models.TextField(verbose_name='댓글 내용')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='생성 날짜')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='마지막 수정 날짜')
