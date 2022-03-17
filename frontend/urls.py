from django.urls import path
from . import views


urlpatterns = [
    path('', views.dtp_sidebar, name='dtp_sidebar')
]
