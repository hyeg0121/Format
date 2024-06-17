from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import Survey, Answer


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


