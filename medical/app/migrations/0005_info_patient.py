# Generated by Django 4.2.3 on 2023-08-05 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_info_numero_remove_systematique_numero_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='patient',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.patient'),
            preserve_default=False,
        ),
    ]
