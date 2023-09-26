from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import QuestionForm


@login_required
def view_help_center(request):
    """ Displays the help center page with a form to ask questions """
    template = "help_center/help_center.html"
    question_form = QuestionForm(initial={"user": request.user})
    question_form.fields['user'].disabled = True

    context = {
        "question_form": question_form,
    }

    return render(request, template, context)
