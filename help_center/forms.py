from django import forms
from .models import Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = (
            "name",
            "email",
            "questions_regarding",
            "message",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
