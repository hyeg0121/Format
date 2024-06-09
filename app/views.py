from django.shortcuts import render, redirect

from app.forms import SurveyForm


def index(request):
    return render(request, 'app/index.html')


def create_survey(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST, request.FILES)
        if form.is_valid():
            survey = form.save(commit=False)
            survey.user = request.user
            survey.save()
            return redirect('index')  # 설문조사 목록 페이지로 리디렉션
    else:
        form = SurveyForm()
    return render(request, 'app/create_survey.html', {'form': form})