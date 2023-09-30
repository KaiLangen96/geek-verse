from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    ORDER = "O"
    DELIVERY = "D"
    RETURN = "R"
    PAYMENT = "P"
    ACCOUNT = "A"
    NEWSLETTER = "N"
    OTHER = "X"

    REASONS = [
        ("ORDER", "the order"),
        ("DELIVERT", "the delivery"),
        ("RETURN", "returning an order"),
        ("PAYMENT", "the payment"),
        ("ACCOUNT", "my account"),
        ("NEWSLETTER", "the newsletter subscription"),
        ("OTHER", "other"),
    ]

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user"
    )
    questions_regarding = models.CharField(
        max_length=254, choices=REASONS, default="O"
    )
    your_question = models.TextField(max_length=500, default="")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"Questions regarding: {self.questions_regarding} from {self.user}"
        )


class Answer(models.Model):
    responder = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="responder"
    )
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="question"
    )
    answer = models.TextField(max_length=500, default="")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Answer regarding: {self.question} from {self.responder}"
