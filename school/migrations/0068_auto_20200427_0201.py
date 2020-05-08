# Generated by Django 2.2.10 on 2020-04-27 02:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('school', '0067_student_code_mined'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='coursesgradesection',
        ),
        migrations.CreateModel(
            name='UserCoursesByYear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(default=2020, verbose_name='Año Lectivo')),
                ('coursesgradesection', models.ManyToManyField(blank=True, to='school.CourseGradeSection', verbose_name='Asignaturas que impartira')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Docente')),
            ],
            options={
                'verbose_name': 'Asignatura por año',
                'verbose_name_plural': 'Asignaturas por año',
                'unique_together': {('user', 'year')},
            },
        ),
    ]