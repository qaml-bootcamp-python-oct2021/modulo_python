#import alumnos
from alumnos import Alumno
import fechas

print(fechas.get_current_date())

m_nombre = 'Marcelo'
m_apellido = 'Equise'
#alumno_01 = alumnos.Alumno(m_nombre, m_apellido)
alumno_01 = Alumno(m_nombre, m_apellido)
alumno_01.set_email('marcelo@email.com')
alumno_01.__curso = 'Java'

'''
java                    python
public variable         variable        accede desde cualquier lugar
private variable        _variable       accede desde cualquier lugar
protected variable      __variable      accede solo desde la instancia de la clase
'''

print(type(alumno_01))
print(alumno_01)
print(alumno_01.get_info())

otro_nombre = 'Juan'
alumno_02 = Alumno(otro_nombre)
print(alumno_02.curso)
#print(alumno_02.__nombre)
print(alumno_02.apellido)
print(alumno_02.email)

k_nombre = 'Kimi'
k_apellido = 'Raikkonen'
k_email = 'kimi@email.com'
alumno_03 = Alumno(nombre=k_nombre, apellido=k_apellido, email=k_email)
print(alumno_03.get_info())