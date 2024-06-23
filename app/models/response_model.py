import djongo.models
from django.db import models
from django.conf import settings


class Response(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='응답자')
    survey = models.ForeignKey('app.Survey', on_delete=models.CASCADE, related_name='responses', verbose_name='설문조사')
    responses = djongo.models.JSONField(default=dict, verbose_name='응답')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='생성 날짜')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='마지막 수정 날짜')

    def __str__(self):
        return f'User ID: {self.user.id}, Survey ID: {self.survey.id}, Responses: {len(self.responses)}'

    class Meta:
        verbose_name = '응답'
        verbose_name_plural = '응답'




