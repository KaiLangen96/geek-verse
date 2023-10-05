from django.shortcuts import (
    render,
    redirect,
    reverse,
    get_object_or_404,
)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

from .forms import QuestionForm, AnswerForm
from .models import Question, Answer


@login_required
def view_help_center(request):
    """Display the help center page with a form to ask questions"""
    template = "help_center/help_center.html"
    question_form = QuestionForm(initial={"user": request.user})
    question_form.fields["user"].disabled = True
    context = {
        "question_form": question_form,
    }
    return render(request, template, context)


@login_required
def submit_question(request):
    """Post the questions to the admin via the question form"""
    if request.method == "POST":
        question_form = QuestionForm(
            request.POST, initial={"user": request.user}
        )
        question_form.fields["user"].disabled = True
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
        question_form.fields["user"].disabled = True
    messages.error(
        request,
        "The question form is invalid. Please ensure the form is valid.",
    )
    template = "help_center/help_center.html"
    context = {
        "question_form": question_form,
    }
    return render(request, template, context)


@login_required
def view_dashboard(request):
    """Display all questions"""
    if not request.user.is_superuser:
        messages.error(
            request,
            "Sorry, only store owners can view the help center dashboard.",
        )
        raise PermissionDenied
    questions = Question.objects.all()
    template = "help_center/help_center_dashboard.html"
    context = {"questions": questions}
    return render(request, template, context)


@login_required
def question_detail(request, question_id):
    """Display a specific questions details"""
    question = get_object_or_404(Question, pk=question_id)
    if request.user == question.user or request.user.is_superuser:
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
    else:
        messages.error(request, "Sorry, you can only view your own questions.")
        raise PermissionDenied


@login_required
def view_answer(request, question_id):
    """Give the admins the possibility to answer questions"""
    if not request.user.is_superuser:
        messages.error(
            request, "Sorry, only store owners can answer questions."
        )
        raise PermissionDenied
    question = get_object_or_404(Question, pk=question_id)
    template = "help_center/answer.html"
    answer_form = AnswerForm(initial={"responder": request.user})
    answer_form.fields["responder"].disabled = True
    context = {
        "question": question,
        "answer_form": answer_form,
    }
    return render(request, template, context)


@login_required
def send_answer(request, question_id):
    """Post the answer to the admin via the answer form"""
    answer_form = AnswerForm(
        data=request.POST, initial={"responder": request.user}
    )
    answer_form.fields["responder"].disabled = True
    redirect_url = request.POST.get("redirect_url_2")
    question = get_object_or_404(Question, pk=question_id)
    if answer_form.is_valid():
        answer_form.instance.question = question
        answer_form.save()
        messages.success(
            request,
            "Your answer has been submitted.",
        )
        return redirect(reverse(view_dashboard))
    else:
        messages.error(
            request,
            "The answer form is invalid. Please ensure the form is valid.",
        )
        template = redirect_url
        context = {
            "answer_form": answer_form,
        }
    return render(request, template, context)


@login_required
def delete_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user == question.user or request.user.is_superuser:
        if request.method == "POST":
            question.delete()
            messages.success(request, "Successfully deleted the question!")
            if request.user.is_superuser:
                return redirect(reverse("view_dashboard"))
            else:
                return redirect(reverse("my_questions"))
        template = "help_center/delete_question.html"
        context = {
            "question": question,
        }
        return render(request, template, context)
    else:
        messages.error(
            request, "Sorry, you can only delete your own questions."
        )
        raise PermissionDenied
