from django.views.generic import (
    ListView,
)

from polls.models import (
    Question,
)

class QuestionListView(ListView):
    model = Question
    ordering = ['-id']
