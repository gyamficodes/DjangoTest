from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    grade = models.CharField(max_length=50)

    # method to return the full name of the student
    def __str__(self):
        return  self.first_name + ' ' + self.last_name
