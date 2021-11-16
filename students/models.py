from django.db import models

class Teacher(models.Model):

    firstname: str = models.CharField(max_length=100)
    surname: str = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'Student {self.firstname}, {self.lastname}'

class Student(models.Model):

    firstname: str= models.CharField(max_length=100)
    surname: str = models.CharField(max_length=100)
    age: int = models.IntegerField()
    classroom: int = models.IntegerField()
    teacher: str = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.firstname

######################################