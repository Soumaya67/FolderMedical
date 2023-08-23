# Generated by Django 4.2.3 on 2023-08-05 16:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_systematique_date_alter_dossiermedical_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='numero',
        ),
        migrations.RemoveField(
            model_name='systematique',
            name='numero',
        ),
        migrations.AddField(
            model_name='systematique',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.DeleteModel(
            name='DossierMedical',
        ),
    ]