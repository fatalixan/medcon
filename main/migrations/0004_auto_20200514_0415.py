# Generated by Django 3.0.5 on 2020-05-14 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200511_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='query_text',
            field=models.FileField(upload_to=''),
        ),
    ]