from django.core.paginator import Paginator
from django.shortcuts import render
from app.models import Survey


def index(request):
    order_by = request.GET.get('order_by', 'latest')
    surveys_list = Survey.objects.all()
    surveys_list = [survey for survey in surveys_list if survey.is_searchable]

    if order_by == 'end_date':
        surveys_list = sorted(surveys_list, key=lambda x: x.end_date)
    elif order_by == 'popularity':
        surveys_list = sorted(surveys_list, key=lambda x: x.responses.count(), reverse=True)
    else:  # 'latest'
        surveys_list = sorted(surveys_list, key=lambda x: x.created_at, reverse=True)

    paginator = Paginator(surveys_list, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'app/index.html', {'page_obj': page_obj})

