from django.db import models


class Teacher(models.Model):
    full_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()

    def __str__(self):
        return f"{self.full_name} {self.date_of_birth}"


class Group(models.Model):
    group = models.CharField(max_length=50)
    curator = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, related_name="groups"
    )

    def __str__(self):
        return f"{self.group} {self.curator}"
