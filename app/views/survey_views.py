from collections import defaultdict

from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..forms import SurveyForm, CommentForm
from ..models import Survey, Comment


@login_required
def create_survey(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST, request.FILES)
        if form.is_valid():
            survey = form.save(commit=False)
            survey.user = request.user
            survey.save()
            return redirect('app:create_question', survey_id=survey.id)  # 문항 추가 페이지로 리디렉션
    else:
        form = SurveyForm()
    return render(request, 'app/page/survey/survey_create.html', {'form': form})


@login_required
def survey_detail(request, survey_id):
    survey = get_object_or_404(Survey, pk=survey_id)
    questions = survey.questions.all()
    is_owner = (survey.user == request.user)
    comments = Comment.objects.filter(survey=survey).select_related('user')
    statistics = defaultdict(lambda: defaultdict(int))
    total_responses = survey.responses.count()

    for response in survey.responses.all():
        for question_id, value in response.responses.items():
            statistics[int(question_id)][value] += 1

    percentages = defaultdict(lambda: defaultdict(float))
    for question_id, counts in statistics.items():
        for option, count in counts.items():
            percentages[question_id][option] = (count / total_responses) * 100 if total_responses > 0 else 0

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.survey = survey
            comment.save()
            return redirect('app:survey_detail', survey_id=survey.id)
    else:
        comment_form = CommentForm()

    return render(request, 'app/page/survey/survey_detail.html', {
        'survey': survey,
        'questions': questions,
        'statistics': statistics,
        'percentages': percentages,
        'is_owner': is_owner,
        'comments': comments,
        'comment_form': comment_form,
    })


@login_required
def survey_update(request, survey_id):
    survey = get_object_or_404(Survey, pk=survey_id)
    if request.user != survey.user:
        pass

    if request.method == 'POST':
        form = SurveyForm(request.POST, instance=survey)
        if form.is_valid():
            form.save()
            return redirect('app:survey_detail', survey_id=survey_id)
    else:
        form = SurveyForm(instance=survey)

    return render(request, 'app/page/survey/survey_update.html', {
        'survey': survey,
        'form': form,
    })


@login_required
def survey_delete(request, survey_id):
    survey = get_object_or_404(Survey, pk=survey_id)
    if request.user != survey.user:
        pass

    if request.method == 'POST':
        survey.delete()
        return redirect('app:user_info')

    return render(request, 'app/page/survey/survey_delete.html', {'survey': survey})


def survey_search(request):
    query = request.GET.get('q', '')

    survey_list = Survey.objects.filter(title__icontains=query)
    survey_list = [survey for survey in survey_list if survey.is_searchable]

    paginator = Paginator(survey_list, 12)  # 페이지 당 12개의 설문조사
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'app/page/survey/survey_search.html', {'page_obj': page_obj, 'query': query})
