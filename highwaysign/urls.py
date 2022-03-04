from django.urls import path
from.views import (home, ClassASignsListView, signs,
                   ClassBSignsListView, ClassCSignsListView,
                    )

urlpatterns = [
    path('', home, name='home'),
    path('signs/', signs, name='signs'),
    path('class-a-signs/', ClassASignsListView.as_view(), name='class-a-signs'),
    path('class-b-signs/', ClassBSignsListView.as_view(), name='class-b-signs'),
    path('class-c-signs/', ClassCSignsListView.as_view(), name='class-c-signs'),
]
