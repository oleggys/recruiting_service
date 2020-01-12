from django.db import models

# Create your models here.
from staff.models import Recruiter, Clan


class Test(models.Model):
    name = models.CharField('Test title', max_length=100)
    clan = models.OneToOneField(Clan, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


class Question(models.Model):
    text = models.TextField('Text')
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class RecruiterAnswer(models.Model):
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.BooleanField('Answer')


class EndTestRecruiter(models.Model):
    recruiter = models.OneToOneField(Recruiter, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
