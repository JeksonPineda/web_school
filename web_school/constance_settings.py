"""
configuraciones para django constances
"""
from datetime import date

year = int(date.today().year)

CONSTANCE_ADDITIONAL_FIELDS = {
    'image_field': ['django.forms.ImageField', {}]
}

# NOTE si cambia el nombre de las key de fecha limite cambiarlo tambien en views linea 146

CONSTANCE_CONFIG = {
    'CANTIDAD_ALUMNOS_POR_AULA': (30, 'La cantidad limite de alumnos por cada aula(Grado Sección)', int),
    'NOTA_MINIMA_APROBADO': (60, 'Nota minima para aprobsar una evaluación(Nota)', int),
    'INTENTOS_PARA_REGISTRAR_NOTA': (2, 'Número de intentos para registrar una nota(Nota)', int),
    'FECHA_LIMITE_REGISTRO_I_BIMENSUAL': (date(year, 6, 29), "Ultima fecha de registro", date),
    'FECHA_LIMITE_REGISTRO_II_BIMENSUAL': (date(year, 8, 29), "Ultima fecha de registro", date),
    'FECHA_LIMITE_REGISTRO_III_BIMENSUAL': (date(year, 10, 29), "Ultima fecha de registro", date),
    'FECHA_LIMITE_REGISTRO_IV_BIMENSUAL': (date(year, 12, 12), "Ultima fecha de registro", date),
    'NOMBRE_DEL_COLEGIO': ('', 'Nombre del Colegio', str),
    'DIRECCION_DEL_COLEGIO': ('', 'Nombre del Colegio', str),
    'TELEFONO_DEL_COLEGIO': ('', 'Nombre del Colegio', str),
    'LOCACION_DEL_COLEGIO': ('', 'Nombre del Colegio', str),
    'LOGO_DEL_COLEGIO': ('', 'Nombre del Colegio', 'image_field'),
}
