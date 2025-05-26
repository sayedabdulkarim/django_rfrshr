from django.db import models

# Create your models here.
class Student(models.Model):
    """
    Model representing a student.
    """
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    email = models.EmailField(unique=True)
    address = models.TextField(blank=True, null=True)
    image = models.ImageField()
    file = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Product(models.Model):
    pass
