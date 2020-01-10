from django.db import models
from django.utils import timezone
# Create your models here.


class Planet(models.Model):
    name = models.CharField('Planet`s name', max_length=50)

    def __str__(self):
        return self.name


class Recruiter(models.Model):
    name = models.CharField('Recruiter`s name', max_length=50)
    birth_date = models.DateField('Birth date')
    email = models.EmailField('Email')
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE)

    def get_age(self):
        today = timezone.now()
        return ((today.date() - self.birth_date) / 365.25).days

    def __str__(self):
        return self.email

    def send_notification(self):
        pass


class Clan(models.Model):
    name = models.CharField('Order`s name', max_length=50)
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Sith(models.Model):
    name = models.CharField('Sith`s name', max_length=50)
    clan = models.ForeignKey(Clan, on_delete=models.CASCADE)

    def __str__(self):
        return '{0} #{1}'.format(self.name, self.id)
