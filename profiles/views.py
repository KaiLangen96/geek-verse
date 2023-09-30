from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order
from help_center.models import Question, Answer


@login_required
def profile(request):
    """Display the user's profile."""
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully")
        else:
            messages.error(
                request, "Update failed. Please ensure the form is valid."
            )
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = "profiles/profile.html"
    context = {"form": form, "orders": orders, "no_cart_display": True}

    return render(request, template, context)


@login_required
def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(
        request,
        (
            f"This is a past confirmation for order number {order_number}. "
            "A confirmation email was sent on the order date."
        ),
    )

    template = "checkout/checkout_success.html"
    context = {
        "order": order,
        "from_profile": True,
    }

    return render(request, template, context)


@login_required
def my_questions(request):
    """Gives the user the possibility to see their questions and answers"""
    questions = Question.objects.filter(user=request.user)
    template = "profiles/my_questions.html"

    context = {
        "questions": questions,
    }

    return render(request, template, context)


@login_required
def my_question_detail(request, question_id):
    """Displays a specific questions details"""
    question = get_object_or_404(Question, pk=question_id)
    answers = Answer.objects.filter(question=question_id)
    if answers.exists():
        answer = answers
    else:
        answer = None
    template = "profiles/my_question_detail.html"

    context = {
        "question": question,
        "answer": answer,
    }
    return render(request, template, context)
