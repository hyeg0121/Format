from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from app.models import Survey, Answer, Comment


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

