from django.contrib import admin
from help_center.models import Question, Answer


class QuestionAdmin(admin.ModelAdmin):
    """Allows admin to manage enquiries via the admin panel"""

    list_display = (
        "id",
        "user",
        "questions_regarding",
        "date",
    )


class AnswerAdmin(admin.ModelAdmin):
    """Allows admin to manage enquiries via the admin panel"""

    list_display = (
        "id",
        "responder",
        "date",
        "question_id",
    )


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
