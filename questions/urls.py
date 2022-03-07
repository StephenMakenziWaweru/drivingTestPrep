from django.urls import path
from .views import (GeneralListView, DefinitionsListView,
                    SignsListView, MtbListView, likeView,
                    QuestionDetailView, QuestionUpdateView,
                    QuestionDeleteView, dislikeView)

urlpatterns = [
    path('', GeneralListView.as_view(), name='general-q'),
    path('definitions/', DefinitionsListView.as_view(), name='definitions-q'),
    path('signs/', SignsListView.as_view(), name='signs-q'),
    path('mtb/', MtbListView.as_view(), name='mtb-q'),
    path('like/<int:pk>', likeView, name='like_quiz'),
    path('dislike/<int:pk>', dislikeView, name='dislike_quiz'),
    path('question-detail/<int:pk>', QuestionDetailView.as_view(), name='question-detail'),
    path('question-edit/<int:pk>', QuestionUpdateView.as_view(), name='question-edit'),
    path('question-delete/<int:pk>', QuestionDeleteView.as_view(), name='question-delete'),
]
