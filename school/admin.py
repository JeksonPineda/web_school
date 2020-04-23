from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from jet.admin import CompactInline
from school.models import (Nationality, Profile, Course,
                           PersonalFile, Student, Grade,
                           Family, Gender, Matriculation,
                           PaperCenter, Note, Section,
                           GradeSection, CourseGradeSection,
                           NoteControlEdition)
from constance.admin import ConstanceAdmin, Config


# Inlines
class ProfileInline(admin.TabularInline):
    model = Profile


class PersonalFileInline(admin.StackedInline):
    model = PersonalFile


class MatriculationInline(CompactInline):
    model = Matriculation
    readonly_fields = ('teaching_year',)


class PaperCenterInline(admin.StackedInline):
    model = PaperCenter


# Admin Class for Catalogs
class CatalogsAdmin(admin.ModelAdmin):
    list_display = ('name', 'active')


class MatriculationAdmin(admin.ModelAdmin):
    readonly_fields = ['teaching_year']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    inlines = [
        PersonalFileInline,
        MatriculationInline,
        PaperCenterInline
    ]

    # show the importants field of the model
    list_display = ('fullname', 'gender', 'nationality', 'status')
    # quantity of register per page
    list_per_page = 20
    # order the registrar by
    ordering = ['-names']
    # convert field to link to go the change form.
    # can be the same fields fo list_display
    list_display_links = ('fullname',)
    # searchible fields
    search_fields = ['names', 'last_name']
    # define the fields that can be selects
    list_filter = [
        'gender',
        'nationality',
        'status'
    ]
    # define the distribution and order of the fields of the model
    fieldsets = [
        ('Información General del Estudiante',
         {'fields': ['names', 'last_name', 'birthday',
                     'gender', 'nationality',
                     'status', 'family_members',
                     'code_mined']}),
    ]

    # method to concat names and last_name field
    def fullname(self, student):
        return u'{names} {last_names}'.format(names=student.names,
                                              last_names=student.last_name)

    # method.short_description, you define a label
    fullname.short_description = 'Nombre Completo del Estudiante'

    class Media:
        js = ('js/validations_registration_student.js',)


@admin.register(Family)
class FamilyAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'family_role', 'tutor')
    list_per_page = 20
    ordering = ['-full_name']
    list_display_links = ('full_name',)
    search_fields = ['full_name', 'family_role']
    list_filter = [
        'family_role',
        'tutor',

    ]
    # define the distribution and order of the fields of the model
    fieldsets = [
        ('Información General del Familiar',
         {'fields': ['full_name', 'document', 'family_role',
                     'mobile', 'cellphone',
                     'tutor', 'occupation']}),
    ]

    class Media:
        css = {
            'all': ('css/own_styles.css',),
        }


@admin.register(PersonalFile)
class PersonalFileAdmin(admin.ModelAdmin):
    list_display = ('student', 'religion', 'origin_center')
    list_per_page = 20
    ordering = ['-student']
    list_display_links = ('student',)
    search_fields = ['student__names', 'student__last_name']
    list_filter = [
        'religion',
        'origin_center',

    ]
    fieldsets = [
        ('Información General de los Expedientes',
         {'fields': ['student', 'have_brothers_center', 'how_many',
                     'religion', 'origin_center',
                     'year_taken_origin_center', 'diseases', 'in_emergencies_call']}),
    ]


@admin.register(PaperCenter)
class PaperCenterAdmin(admin.ModelAdmin):
    list_display = ('student', 'diploma', 'birth_certificate')
    list_per_page = 20
    ordering = ['-student']
    list_display_links = ('student',)
    search_fields = ['student__names', 'student__last_name']
    list_filter = [
        'diploma',
        'birth_certificate',
    ]
    fieldsets = [
        ('Información General de los Papeles del Centro',
         {'fields': ['student', 'academic_notes', 'diploma',
                     'birth_certificate', 'conduct_certificate',
                     'observations']}),
    ]


class MyUserAdmin(UserAdmin):
    inlines = [ProfileInline]


class ConfigAdmin(ConstanceAdmin):
    pass


# Unregister Models
admin.site.unregister(User)
admin.site.unregister([Config])

# Register your models here.
admin.site.register(Nationality, CatalogsAdmin)
admin.site.register(Course, CatalogsAdmin)
admin.site.register(Gender, CatalogsAdmin)
admin.site.register(Grade, CatalogsAdmin)
admin.site.register(Section, CatalogsAdmin)
admin.site.register(Profile)
admin.site.register(Matriculation, MatriculationAdmin)
admin.site.register(Note)
admin.site.register(GradeSection)
admin.site.register(CourseGradeSection)
admin.site.register(NoteControlEdition)
admin.site.register(User, MyUserAdmin)
admin.site.register([Config], ConfigAdmin)
