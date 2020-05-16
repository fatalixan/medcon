from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Query(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    date_of_creation = models.DateTimeField(default=timezone.now)
    query_text = models.TextField()
    files_name = models.FileField(blank=True)

    class Meta:
        verbose_name = "Запрос на консультацию"
        verbose_name_plural = "Запросы на консультации"



class Consultation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    query = models.ForeignKey(Query, on_delete=models.CASCADE, default=0)
    medical_report = models.TextField("Report")
    date_of_consultation = models.DateTimeField()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    tnumber = models.CharField(max_length=50)
    sex = models.BooleanField()
    lang = models.CharField(max_length=3)

class Medical_record(models.Model):
    information = models.CharField(max_length=255)
    pass

class Consultation_status(models.Model):

    name = models.CharField("Consultation status", max_length=50)




