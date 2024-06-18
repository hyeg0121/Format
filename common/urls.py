from django.urls import path
from .views import EmailLoginView
from . import views
from django.contrib.auth import views as auth_views

app_name = 'common'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', EmailLoginView.as_view(), name='login'),
    path('logout/',  auth_views.LogoutView.as_view(), name='logout'),
]
