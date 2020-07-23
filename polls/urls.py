from django.urls import path

from polls.views import (
    QuestionListView,
)

app_name = 'polls'

urlpatterns = [
    path('', QuestionListView.as_view(), name='question-list'),
]
