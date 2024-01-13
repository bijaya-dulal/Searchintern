from django.db import models

# Create your models here.
class RecruiterForm(models.Model):
    internship_title = models.CharField(max_length=255)
    address = models.TextField()
    description = models.TextField()
    deadline = models.DateField()
    category = models.CharField(max_length=50)
    timing = models.CharField(max_length=50)
    form_due_date = models.DateField()