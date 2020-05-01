from django.db import models

# Create your models here.

class Query(models.Model):

    date_of_creation = models.DateTimeField("Date of creation")
    query_text = models.TextField("Query text")
    files_name = models.CharField("Files name", max_length=255)

class Consultation(models.Model):

    medical_report = models.TextField("Report")
    date_of_consultation = models.DateTimeField

class User(models.Model):

    email = models.CharField(max_length=45)
    password = models.CharField(max_length=20)
    date_of_registration = models.DateTimeField

class Profile(models.Model):

    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    tnumber = models.CharField(max_length=50)
    bday = models.DateField
    sex = models.BooleanField
    lang = models.CharField(max_length=3)

class Medical_record(models.Model):
    pass

class Consultation_status(models.Model):

    name = models.CharField("Consultation status", max_length=50)

class Auth_group(models.Model):

    name = models.CharField(max_length=30)

class Auth_permission(models.Model):
    pass

class Auth_permission_group(models.Model):
    pass

class Content(models.Model):
    name = models.CharField(max_length=30)


