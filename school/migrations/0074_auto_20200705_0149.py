# Generated by Django 2.2.13 on 2020-07-05 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0073_auto_20200628_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notecontroledition',
            name='edit_field',
            field=models.CharField(max_length=15, verbose_name='Campo Edición'),
        ),
    ]
