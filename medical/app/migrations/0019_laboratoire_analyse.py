# Generated by Django 4.2.3 on 2023-08-20 22:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_laboratoire'),
    ]

    operations = [
        migrations.AddField(
            model_name='laboratoire',
            name='analyse',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.analyse'),
            preserve_default=False,
        ),
    ]
