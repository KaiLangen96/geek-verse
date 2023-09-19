from django.db import models


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

    name = models.CharField(max_length=122, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    questions_regarding = models.CharField(
        max_length=254, choices=REASONS, default="O")
    message = models.TextField(max_length=500, default="")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Questions regarding: {self.questions_regarding} from {self.name}"
