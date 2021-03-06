# Generated by Django 3.0.3 on 2020-02-27 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0011_auto_20200227_2226'),
    ]

    operations = [
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50, verbose_name='Nombre Completo')),
                ('document', models.CharField(max_length=16, unique=True, verbose_name='Cedula')),
                ('family_role', models.CharField(choices=[('PAPA', 'PAPA'), ('MAMA', 'MAMA'), ('HERMANO/A', 'HERMANO/A'), ('TIO/A', 'TIO/A'), ('ABUELO/A', 'ABUELO/A')], max_length=20, verbose_name='Rol Familiar')),
                ('mobile', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Celular')),
                ('cellphone', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Teléfono')),
                ('tutor', models.BooleanField(default=False, verbose_name='Tutor')),
                ('occupation', models.CharField(blank=True, max_length=30, verbose_name='Ocupación')),
            ],
        ),
    ]
