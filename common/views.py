from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import FormView

from common.forms import UserCreationForm, EmailLoginForm, UserChangeForm


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # 사용자를 로그인 시킵니다
            login(request, user)
            return redirect('app:index')
    else:
        form = UserCreationForm()
    return render(request, 'common/signup.html', {'form': form})


class EmailLoginView(FormView):
    form_class = EmailLoginForm
    template_name = 'common/login.html'

    def form_valid(self, form):
        email = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
            return redirect('app:index')  # 로그인 후 리디렉션할 URL
        return self.form_invalid(form)

