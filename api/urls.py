from django.urls import path
from . import views


urlpatterns = [
    path('', views.api_overview, name='api-overview'),
    
    # Questions
    path('question-list/', views.question_list, name='question-list-api'),
    path('question-detail/<str:pk>/', views.question_detail, name='question-detail-api'),
    path('question-create/', views.question_create, name='question-create-api'),
    path('question-update/<str:pk>/', views.question_update, name='question-update-api'),
    path('question-delete/<str:pk>/', views.question_delete, name='question-delete-api'),

    # User
    path('user-detail/<str:pk>/', views.user_detail, name='user-detail-api'),
]
