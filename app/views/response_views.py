from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from ..forms import SurveyResponseForm
from ..models import Survey, Response


@login_required
def survey_response(request, survey_id):
    survey = get_object_or_404(Survey, id=survey_id)

    if request.method == 'POST':
        form = SurveyResponseForm(request.POST, survey=survey)
        if form.is_valid():
            responses = form.cleaned_data
            response_obj = Response.objects.create(user=request.user, survey=survey, responses=responses)
            return redirect('app:survey_detail', survey_id=survey.id)
    else:
        form = SurveyResponseForm(survey=survey)

    return render(request, 'app/page/response/survey_response.html', {'survey': survey, 'form': form})


