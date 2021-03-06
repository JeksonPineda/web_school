# Generated by Django 2.2.10 on 2020-04-16 02:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0063_auto_20200416_0214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='family',
            name='cellphone',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(11111111, 'El Teléfono debene tener 8 digitos'), django.core.validators.MaxValueValidator(11111111, 'El Teléfono debene tener 8 digitos')], verbose_name='Teléfono'),
        ),
        migrations.AlterField(
            model_name='family',
            name='mobile',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(11111111, 'El Celular debene tener 8 digitos'), django.core.validators.MaxValueValidator(11111111, 'El Celular debene tener 8 digitos')], verbose_name='Celular'),
        ),
    ]
