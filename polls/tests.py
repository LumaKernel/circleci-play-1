from django.test import TestCase
from django.urls import reverse

from polls.models import Question


class QuestionListViewTest(TestCase):
    def test(self):
        Question.objects.create(desc='why')
        Question.objects.create(desc='how')
        Question.objects.create(desc='what')
        response = self.client.get(reverse('polls:question-list'))
        self.assertQuerysetEqual(
            response.context.get('question_list'),
            [
                '<Question: what>',
                '<Question: how>',
                '<Question: why>',
            ]
        )
