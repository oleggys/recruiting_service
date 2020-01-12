from django.core.mail import EmailMessage, send_mail
from django.db import models
from django.template.loader import get_template
from django.utils import timezone
# Create your models here.
from recruiting_service import settings


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

    def send_notification(self, subject, template_name, context=None):
        from_email, to = settings.EMAIL_HOST_USER, self.email
        html_content = get_template(template_name=template_name).render(context)
        msg = EmailMessage(subject, html_content, from_email, [to])
        msg.content_subtype = 'html'
        msg.send()


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

    def count_of_dark_hand(self):
        return len(DarkHand.objects.filter(sith=self))


class DarkHand(models.Model):
    sith = models.ForeignKey(Sith, on_delete=models.CASCADE)
    recruiter = models.OneToOneField(Recruiter, on_delete=models.CASCADE)