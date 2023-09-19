from django.contrib import admin
from help_center.models import Question


class QuestionAdmin(admin.ModelAdmin):
    """Allows admin to manage enquiries via the admin panel"""

    list_display = (
        "name",
        "email",
        "questions_regarding",
        "date",
    )


admin.site.register(Question, QuestionAdmin)
