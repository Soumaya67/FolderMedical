# Generated by Django 4.2.3 on 2023-08-15 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_analyse_systematique_analyses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='systematique',
            name='analyses',
            field=models.ManyToManyField(to='app.analyse'),
        ),
    ]
