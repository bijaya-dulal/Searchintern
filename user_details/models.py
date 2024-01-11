from django.db import models

# Create your models here.
class User_details(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=500)  # You might want to consider using Django's built-in authentication system.
    category = models.CharField(max_length=50)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)


