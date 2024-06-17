from django.urls import path
from . import views

app_name = 'app'  # 앱 이름 설정

urlpatterns = [
    path('', views.index, name='index'),
    path('mypage/', views.mypage, name='my_page'),
    path('survey/create/', views.create_survey, name='create_survey'),
    path('survey/<int:survey_id>/questions/', views.create_question, name='create_question'),
    path('survey/<int:survey_id>/', views.survey_detail, name='survey_detail'),
    path('survey/<int:survey_id>/response/', views.survey_response, name='survey_response'),
    path('survey/<int:survey_id>/update/', views.survey_update, name='survey_update'),
    # path('survey/<int:survey_id>/delete/', views.survey_delete, name='survey_delete'),
]
