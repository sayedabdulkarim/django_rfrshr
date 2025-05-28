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
    image = models.ImageField(blank=True, null=True)
    file = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Car(models.Model):
    """
    Model representing a car.
    """
    name = models.CharField(max_length=100)
    speed = models.PositiveIntegerField(default=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name