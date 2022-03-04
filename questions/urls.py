from django.urls import path
from .views import (GeneralListView, DefinitionsListView,
                    SignsListView, MtbListView, likeView)

urlpatterns = [
    path('', GeneralListView.as_view(), name='general-q'),
    path('definitions/', DefinitionsListView.as_view(), name='definitions-q'),
    path('signs/', SignsListView.as_view(), name='signs-q'),
    path('mtb/', MtbListView.as_view(), name='mtb-q'),
    path('like/<int:pk>', likeView, name='like_quiz'),
]
