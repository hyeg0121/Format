from django.urls import path
from .views import index, user_info, create_survey, create_question, survey_detail, survey_response, survey_update, \
    survey_delete, comment_update, comment_delete, survey_search, response_update, response_delete

app_name = 'app'  # 앱 이름 설정

urlpatterns = [
    path('', index, name='index'),
    path('user/', user_info, name='user_info'),
    # survey
    path('survey/create/', create_survey, name='create_survey'),
    path('survey/<int:survey_id>/questions/', create_question, name='create_question'),
    path('survey/<int:survey_id>/', survey_detail, name='survey_detail'),
    path('survey/<int:survey_id>/response/', survey_response, name='survey_response'),
    path('survey/<int:survey_id>/update/', survey_update, name='survey_update'),
    path('survey/<int:survey_id>/delete/', survey_delete, name='survey_delete'),
    path('survey/search/', survey_search, name='survey_search'),
    # comment
    path('comment/<int:comment_id>/update', comment_update, name='comment_update'),
    path('comment/<int:comment_id>/delete', comment_delete, name='comment_delete'),
    # response
    path('response/<int:response_id>/update', response_update, name='response_update'),
    path('response/<int:response_id>/delete', response_delete, name='response_delete'),
]
