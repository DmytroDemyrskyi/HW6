from django.shortcuts import render, redirect

from .forms import TeacherForm, GroupForm

from .models import Teacher, Group


# Create your views here.


def teacher_form(request):
    if request.method == "GET":
        form = TeacherForm()
        return render(request, "teacher_form.html", {"form": form})
    form = TeacherForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect("teacher_list")

    return render(request, "teacher_form.html", {"form": form})


def teachers_list(request):
    teachers = Teacher.objects.all()
    return render(request, "teacher_list.html", {"teachers": teachers})


def group_form(request):
    if request.method == "GET":
        form = GroupForm()
        return render(request, "group_form.html", {"form": form})

    form = GroupForm(request.POST)
    if form.is_valid():
        group = form.cleaned_data["group"]
        curator = form.cleaned_data["curator"]

        group, created = Group.objects.get_or_create(
            group=group, defaults={"curator": curator}
        )

        if not created:
            group.curator = curator
            group.save()

        return redirect("groups_list")

    return render(request, "group_form.html", {"form": form})


def groups_list(request):
    groups = Group.objects.all()
    return render(request, "group_list.html", {"groups": groups})
