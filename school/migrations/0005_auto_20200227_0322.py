# Generated by Django 3.0.3 on 2020-02-27 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='Nombre'),
        ),
    ]
