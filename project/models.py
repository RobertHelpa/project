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
    name = models.CharField(max_length=124)
    class_group = models.ForeignKey(Class, on_delete=models.CASCADE)
    grades = models.ManyToManyField(Subject, through="Grade") 

    def __str__(self):
        return self.name
    
class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade = models.IntegerField()
    
    def __str__(self) -> str:
        return self.student
    
class Schedule(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    class_group = models.ForeignKey(Class, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    start = models.TimeField()
    end = models.TimeField()
    time = models.TimeField()
    date = models.DateField()

    def __str__(self) -> str:
        return self.subject