from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test, login_required

from .forms import QuestionForm
from .models import Question, Answer


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


@login_required
def submit_question(request):
    """ Posts the questions to the admin via the contact form """
    if request.method == 'POST':
        question_form = QuestionForm(request.POST, initial={"user": request.user})
        question_form.fields['user'].disabled = True

        if question_form.is_valid():
            question = question_form.save()
            template = "help_center/question_submitted.html"
            context = {
                "user": request.user,
                "question": question,
            }
            return render(request, template, context)
    else:
        question_form = QuestionForm(initial={"user": request.user})
        question_form.fields['user'].disabled = True

    messages.error(
        request, "The question form is invalid. Please ensure the form is valid."
    )
    template = "help_center/help_center.html"
    context = {
        "question_form": question_form,
    }
    return render(request, template, context)


@user_passes_test(lambda u: u.is_superuser)
def view_dashboard(request):
    """ Displays all questions """
    questions = Question.objects.all()
    template = "help_center/help_center_dashboard.html"

    context = {
        "questions": questions
    }
    return render(request, template, context)


@login_required
def question_detail(request, question_id):
    """ Displays a specific questions details """
    question = get_object_or_404(Question, pk=question_id)
    answers = Answer.objects.filter(question=question_id)
    if answers.exists():
        answer = answers
    else:
        answer = None
    template = "help_center/question_detail.html"

    context = {
        "question": question,
        "answer": answer,
    }
    return render(request, template, context)
