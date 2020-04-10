from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from school.models import (Nationality, Profile, Course,
                           PersonalFile, Student, Grade,
                           Family, Gender, Matriculation,
                           PaperCenter, Note, Section,
                           GradeSection, CourseGradeSection,
                           NoteControlEdition)


class ProfileInline(admin.TabularInline):
    model = Profile


# Admin Class for Catalogs
class CatalogsAdmin(admin.ModelAdmin):
    list_display = ('name', 'active')


class MatriculationAdmin(admin.ModelAdmin):
    readonly_fields = ['teaching_year']


class MyUserAdmin(UserAdmin):
    inlines = [ProfileInline]


# Unregister Models
admin.site.unregister(User)

# Register your models here.
admin.site.register(Nationality, CatalogsAdmin)
admin.site.register(Course, CatalogsAdmin)
admin.site.register(Gender, CatalogsAdmin)
admin.site.register(Grade, CatalogsAdmin)
admin.site.register(Section, CatalogsAdmin)
admin.site.register(Profile)
admin.site.register(PersonalFile)
admin.site.register(Student)
admin.site.register(Family)
admin.site.register(Matriculation, MatriculationAdmin)
admin.site.register(PaperCenter)
admin.site.register(Note)
admin.site.register(GradeSection)
admin.site.register(CourseGradeSection)
admin.site.register(NoteControlEdition)
admin.site.register(User, MyUserAdmin)
