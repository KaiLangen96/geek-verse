from django.urls import path
from . import views

urlpatterns = [
    path("", views.view_help_center, name="view_help_center"),
    path("submit/", views.submit_question, name="submit_question"),
    path("dashboard/", views.view_dashboard, name="view_dashboard"),
    path(
        "dashboard/<int:question_id>/",
        views.question_detail,
        name="question_detail",
    ),
    path("answer/<int:question_id>/", views.view_answer, name="view_answer"),
    path(
        "send_answer/<int:question_id>/", views.send_answer, name="send_answer"
    ),
    path(
        "delete/<int:question_id>/",
        views.delete_question,
        name="delete_question",
    ),
]
