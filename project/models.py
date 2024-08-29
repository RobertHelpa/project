from django.db import models

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=124)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class Teacher(models.Model):
    name = models.CharField(max_length=124)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Class(models.Model):
    name = models.CharField(max_length=124)
    year = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    
class Student(models.Model):
    name = models.CharField(max_length=12)
    class_group = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return self.name