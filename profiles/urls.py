from django.urls import path
from . import views

urlpatterns = [
    path("", views.profile, name="profile"),
    path(
        "order_history/<order_number>",
        views.order_history,
        name="order_history",
    ),
    path("my_questions/", views.my_questions, name="my_questions"),
    path(
        "my_questions/<int:question_id>/",
        views.my_question_detail,
        name="my_question_detail",
    ),
]
