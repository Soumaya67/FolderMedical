# Generated by Django 4.2.3 on 2023-08-10 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_patient_info_info_patient'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisiteReprise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('apte', models.BooleanField()),
                ('texte_certificat', models.TextField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visites_reprise', to='app.patient')),
            ],
        ),
    ]
