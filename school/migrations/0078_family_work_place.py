# Generated by Django 2.2.13 on 2020-09-13 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0077_family_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='family',
            name='work_place',
            field=models.CharField(default='', max_length=100, verbose_name='Lugar de trabajo'),
        ),
    ]
