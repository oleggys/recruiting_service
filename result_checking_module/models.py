from django.db import models

# Create your models here.
from staff.models import Recruiter


class Test(models.Model):
    order = models.IntegerField('Unique order number', unique=True)

    def __str__(self):
        return str(self.order)


class Question(models.Model):
    text = models.TextField('Text')
    order = models.ForeignKey(Test, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class RecruiterAnswer(models.Model):
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.BooleanField('Answer')
