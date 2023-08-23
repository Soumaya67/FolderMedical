# Generated by Django 4.2.3 on 2023-08-20 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_alter_surveillance_a_v_alter_surveillance_albumin_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Laboratoire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fichier', models.FileField(upload_to='analyses/')),
                ('systematique', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.systematique')),
            ],
        ),
    ]