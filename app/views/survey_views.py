from collections import defaultdict
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
    return render(request, 'app/page/survey/create_survey.html', {'form': form})


@login_required
def survey_detail(request, survey_id):
    survey = get_object_or_404(Survey, pk=survey_id)
    questions = survey.questions.all()
    is_owner = (survey.user == request.user)
    comments = Comment.objects.filter(survey=survey).select_related('user')
    statistics = defaultdict(lambda: defaultdict(int))

    for answer in survey.answers.all():
        for question_id, response in answer.responses.items():
            statistics[int(question_id)][response] += 1

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
        return redirect('app:my_page')

    return render(request, 'app/page/survey/survey_delete.html', {'survey': survey})