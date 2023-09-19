from django.shortcuts import render

from .forms import QuestionForm


def view_help_center(request):
    """Displays the help center page"""
    template = "help_center/help_center.html"

    if request.user.is_authenticated:
        question_form = QuestionForm(initial={"email": request.user.email})
    else:
        question_form = QuestionForm()

    context = {
        "question_form": question_form,
    }

    return render(request, template, context)
