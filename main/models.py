from django.db import models
from django.db.models import CASCADE


class CV(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    bio = models.TextField()

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class Skill(models.Model):
    name = models.CharField(max_length=100)
    cv = models.ForeignKey(CV, on_delete=CASCADE, related_name="skills")

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    link = models.URLField()
    cv = models.ForeignKey(CV, on_delete=CASCADE, related_name="projects")


    def __str__(self):
        return self.name


class Contact(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    linkedin = models.URLField(blank=True, null=True)
    cv = models.ForeignKey(CV, on_delete=CASCADE, related_name="contacts")

    def __str__(self):
        return self.email
