from django.urls import path
from .views import (introduction, NotesListView, VideosListView,
                    notes_delete_view, NotesUpdateView)

urlpatterns = [
    path('', introduction, name='mtb-intro'),
    path('notes/', NotesListView.as_view(), name='mtb-notes'),
    path('notes-delete/<str:id>/', notes_delete_view, name='notes-delete'),
    path('notes-edit/<str:pk>/', NotesUpdateView.as_view(), name='notes-edit'),
    path('videos/', VideosListView.as_view(), name='mtb-videos'),
]
