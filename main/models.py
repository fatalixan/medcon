from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Query(models.Model):

    date_of_creation = models.DateTimeField("Date of creation")
    query_text = models.TextField("Query text")
    files_name = models.CharField("Files name", max_length=255)

class Consultation(models.Model):

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




