from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views.generic import FormView

from common import forms
from common.forms import UserCreationForm, EmailLoginForm


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('common:login')
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

