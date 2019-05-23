from django.db import models

# Create your models here.


class Discipline(models.Model):
    name = models.CharField(max_length=50)
    info = models.TextField()


    def __str__(self):
        return self.name


class Test(models.Model):
    name = models.CharField(max_length=50)
    info = models.TextField()


    def __str__(self):
        return self.name


class Question(models.Model):
    name = models.TextField()
    answer1 = models.TextField()
    answer2 = models.TextField()
    answer3 = models.TextField()
    answer4 = models.TextField()
    rigth_answer = models.IntegerField()

    def __str__(self):
        return self.name