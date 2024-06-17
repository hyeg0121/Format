from django.shortcuts import render

from app.models import Survey


def index(request):
    surveys = Survey.objects.all()  # 모든 설문조사 가져오기
    return render(request, 'app/index.html', {'surveys': surveys})
