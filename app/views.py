from collections import defaultdict

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import SurveyForm, QuestionForm, SurveyResponseForm, CommentForm
from .models import Survey, Question, Answer, Comment


def index(request):
    surveys = Survey.objects.all()  # 모든 설문조사 가져오기
    return render(request, 'app/index.html', {'surveys': surveys})


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
    return render(request, 'app/survey/create_survey.html', {'form': form})


@login_required
def create_question(request, survey_id):
    survey = get_object_or_404(Survey, pk=survey_id)
    questions = Question.objects.filter(survey=survey)

    if request.method == "POST":
        form = QuestionForm(request.POST)

        if form.is_valid():
            # 요청에서 options_json 가져오기
            options_json = request.POST.get('options_json')

            question = form.save(commit=False)
            question.survey = survey
            question.options = options_json
            question.save()

            if 'add_question' in request.POST:
                # 문항 추가인 경우 app:create_question 으로 이동
                return redirect('app:create_question', survey_id=survey.id)
            # 저장인 경우 설문조사 상세 페이지로 이동함
            return redirect('app:survey_detail', survey_id=survey.id)
    else:
        form = QuestionForm()

    return render(request, 'app/question/create_question.html',
                  {'form': form, 'survey': survey, 'questions': questions})


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

    return render(request, 'app/survey/survey_detail.html', {
        'survey': survey,
        'questions': questions,
        'statistics': statistics,
        'is_owner': is_owner,
        'comments': comments,
        'comment_form': comment_form,
    })


@login_required
def mypage(request):
    user = request.user
    surveys = Survey.objects.filter(user=user)
    answers = Answer.objects.filter(user=user).select_related('survey')
    comments = Comment.objects.filter(user=user).select_related('survey')

    return render(request, 'app/mypage/mypage.html',
                  {
                      'user': user,
                      'surveys': surveys,
                      'answers': answers,
                      'comments': comments,
                  })


@login_required
def survey_response(request, survey_id):
    survey = get_object_or_404(Survey, id=survey_id)
    if request.method == 'POST':
        responses = {}
        for question in survey.questions.all():
            key = str(question.pk)
            response = request.POST.get(key, '')  # 기본값으로 빈 문자열을 설정
            responses[key] = response

        # 응답 저장
        Answer.objects.create(user=request.user, survey=survey, responses=responses)
        return redirect('app:survey_detail', survey_id=survey_id)

    return render(request, 'app/response/survey_response.html', {'survey': survey})


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

    return render(request, 'app/survey/survey_update.html', {
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

    return render(request, 'app/survey/survey_delete.html', {'survey': survey})