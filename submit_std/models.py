from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    skills = models.TextField()
    sskill = models.CharField(max_length=255)
    college = models.CharField(max_length=255)
    course = models.CharField(max_length=255)
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)

