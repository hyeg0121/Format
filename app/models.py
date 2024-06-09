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
        return self.title

    class Meta:
        verbose_name = '설문조사'
        verbose_name_plural = '설문조사'
