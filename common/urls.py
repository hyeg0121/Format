from django.urls import path
from .views import EmailLoginView
from . import views

app_name = 'common'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', EmailLoginView.as_view(), name='login'),
]
