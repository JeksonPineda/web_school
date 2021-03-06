def build_django_jet_menu():
    return [
        {
            'label': 'Roles y Usuarios',
            'permissions': [
                'request.user.is_superuser'
            ],
            'items': [
                {
                    'name': 'auth.group',
                    'label': 'Listado roles',
                    'permissions': [
                        'auth.add_group',
                        'auth.change_group'
                    ]
                },
                {
                    'name': 'auth.user',
                    'label': 'Listado usuarios',
                    'permissions': [
                        'request.user.is_superuser'
                    ]
                }
            ]
        },
        {
            'label': 'Variables de sistema',
            'permissions': [
                'request.user.is_superuser'
            ],
            'items': [
                {
                    'name': 'constance.config',
                    'label': 'Variables',
                }
            ]
        },
        {
            'label': 'Catalogos',
            'permissions': [],
            'items': [
                {
                    'name': 'school.course',
                    'label': 'Asignaturas',
                    'permissions': [
                        'school.view_course'
                    ]
                },
                {
                    'name': 'school.profile',
                    'label': 'Docentes',
                    'permissions': [
                        'school.view_profile'
                    ]
                },
                {
                    'name': 'school.grade',
                    'label': 'Grados',
                    'permissions': [
                        'school.view_grade'
                    ]
                },
                {
                    'name': 'school.section',
                    'label': 'Sección',
                    'permissions': [
                        'school.view_section'
                    ]
                },
                {
                    'name': 'school.gender',
                    'label': 'Géneros',
                    'permissions': [
                        'school.view_gender'
                    ]
                },
                {
                    'name': 'school.nationality',
                    'label': 'Nacionalidades',
                    'permissions': [
                        'school.view_nationality'
                    ]
                },
                {
                    'name': 'school.gradesection',
                    'label': 'Aulas',
                    'permissions': [
                        'school.view_gradesection'
                    ]
                },
                {
                    'name': 'school.coursegradesection',
                    'label': 'Asignaturas Por Aulas',
                    'permissions': [
                        'school.view_coursegradesection'
                    ]
                },

            ]
        },
        {
            'label': 'Registro nuevo estudiante',
            'permissions': [
                'school.view_student',
                'school.view_personalfile',
                'school.view_family',
                'school.view_matriculation',
                'school.view_PaperCenter'
            ],
            'items': [
                {
                    'name': 'school.student',
                    'label': 'Listado estudiantes',
                    'permissions': [
                        'school.view_student'
                    ]
                },
                {
                    'name': 'school.personalfile',
                    'label': 'Expedientes Personales',
                    'permissions': [
                        'school.view_personalfile'
                    ]
                },
                {
                    'name': 'school.family',
                    'label': 'Familiares',
                    'permissions': [
                        'school.view_family'
                    ]
                },
                {
                    'name': 'school.matriculation',
                    'label': 'Matricula',
                    'permissions': [
                        'school.view_matriculation'
                    ]
                },
                {
                    'name': 'school.papercenter',
                    'label': 'Papeles para el centro',
                    'permissions': [
                        'school.view_papercenter'
                    ]
                }
            ]
        },
        {
            'label': 'Estudiantes de reingreso',
            'permissions': [
                'school.view_matriculation'
            ],
            'items': [
                {
                    'name': 'school.matriculation',
                    'label': 'Matricula',
                    'permissions': [
                        'school.view_matriculation'
                    ]
                },
            ]
        }

    ]
