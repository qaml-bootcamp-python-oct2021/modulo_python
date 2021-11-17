from alumnos import Alumno
import fechas

print(fechas.get_current_date())
s_nombre = 'Santiago'
s_apellido = 'Hernandez'
santiago = Alumno(s_nombre,s_apellido)
santiago.set_email('santiago@mail.com')
santiago.__email = 'nuevoemail@mail.com'
print(santiago.get_info())

print('-------------------------')

k_nombre = 'Kimi'
k_apellido = 'Raikkonen'
k_mail = 'kimi@mail.com'
kimi = Alumno(nombre=k_nombre,apellido=k_apellido,email=k_mail)
print(kimi.get_info())

# Java                    Python
# public variable         variable        (Se accede desde cualquier lugar)
# private variable        _variable       (Se accede desde cualquier lugar)
# protected variable      __variable      (Se accede solo desde su propia instancia)