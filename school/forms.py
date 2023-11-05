from django import forms

from school.models import Teacher, Group


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ["full_name", "date_of_birth"]

    def clean_name(self):
        full_name = self.cleaned_data["full_name"]
        if len(full_name) > 50:
            raise forms.ValidationError("Name is too long")
        return full_name


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ["group", "curator"]

    def clean_name(self):
        name = self.cleaned_data["group"]
        if len(name) > 50:
            raise forms.ValidationError("Name is too long")
        return name
