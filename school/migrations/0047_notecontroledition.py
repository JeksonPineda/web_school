# Generated by Django 2.2.10 on 2020-04-06 02:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('school', '0046_note_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='NoteControlEdition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edit_field', models.CharField(max_length=10, verbose_name='Campo Edición')),
                ('value_edit_field', models.IntegerField(verbose_name='Valor')),
                ('registration_date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Registro')),
                ('note', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Note', verbose_name='Nota')),
                ('supervisor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Supervisor')),
            ],
            options={
                'verbose_name': 'Nota Control Edición',
                'verbose_name_plural': 'Notas Control Edición',
            },
        ),
    ]
