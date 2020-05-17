from django.db.models.fields.files import FieldFile
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Query(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    date_of_creation = models.DateTimeField(default=timezone.now)
    query_text = models.TextField()


    class Meta:
        verbose_name = "Запрос на консультацию"
        verbose_name_plural = "Запросы на консультации"

class Files(models.Model):
    file = models.FileField(upload_to='files', blank=True, null=True, verbose_name="Файл")
    files = models.ForeignKey(Query, blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Файлы"
        verbose_name_plural = "Файлы"



class Consultation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    query = models.ForeignKey(Query, on_delete=models.CASCADE, default=0)
    medical_report = models.TextField("Report")
    date_of_consultation = models.DateTimeField()

    class Meta:
        verbose_name = "Консультация"
        verbose_name_plural = "Консультации"

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




