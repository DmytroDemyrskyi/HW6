from django.urls import path

from .views import teacher_form, teachers_list, group_form, groups_list

urlpatterns = [
    path("teacher/", teacher_form, name="teacher_form"),
    path("teachers/", teachers_list, name="teacher_list"),
    path("group/", group_form, name="group_form"),
    path("groups/", groups_list, name="groups_list"),
]
