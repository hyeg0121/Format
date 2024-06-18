from django.urls import path
from .views import index, user_info, create_survey, create_question, survey_detail, survey_response, survey_update, \
    survey_delete

app_name = 'app'  # 앱 이름 설정

urlpatterns = [
    path('', index, name='index'),
    path('user/', user_info, name='user_info'),
    path('survey/create/', create_survey, name='create_survey'),
    path('survey/<int:survey_id>/questions/', create_question, name='create_question'),
    path('survey/<int:survey_id>/', survey_detail, name='survey_detail'),
    path('survey/<int:survey_id>/response/', survey_response, name='survey_response'),
    path('survey/<int:survey_id>/update/', survey_update, name='survey_update'),
    path('survey/<int:survey_id>/delete/', survey_delete, name='survey_delete'),
]
