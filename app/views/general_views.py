from django.core.paginator import Paginator
from django.shortcuts import render
from app.models import Survey


def index(request):
    surveys_list = Survey.objects.all()  # 모든 설문조사 가져오기

    paginator = Paginator(surveys_list, 9)  # 페이지당 12개씩 분할
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'app/index.html', {'page_obj': page_obj})
