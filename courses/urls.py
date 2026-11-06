
from django.urls import path
from .views import (
    TeacherListView,
    CourseListView,
    StudentListView
)


urlpatterns = [
    path("teachers/", TeacherListView.as_view()),
    path("courses/", CourseListView.as_view()),
    path("students/", StudentListView.as_view()),
]
