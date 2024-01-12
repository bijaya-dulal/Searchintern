from django.db import models

class Student_info(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=15)  # Assuming phone numbers as strings
    address = models.TextField()
    college = models.CharField(max_length=255)
    course = models.CharField(max_length=100)
    semester = models.PositiveIntegerField()
    skill = models.TextField()
    start_date = models.DateField()
    duration = models.PositiveIntegerField()  # Assuming duration in months
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    cv = models.FileField(upload_to='cv_pdfs/')
# Create your models here.
