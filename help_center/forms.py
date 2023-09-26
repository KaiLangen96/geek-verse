from django import forms
from .models import Question, Answer


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = (
            "user",
            "questions_regarding",
            "your_question",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = (
            "responder",
            "answer",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
