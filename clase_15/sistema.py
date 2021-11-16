from tarea import Tarea
from usuario import Usuario

tareas = []
usuarios = []

d = Usuario('David', 'david@gmail.com')
usuarios.append(d)
#guardar usuarios en archivo

p = Usuario('Pepito', 'pepito@gmail.com')
usuarios.append(p)

t = Tarea('tarea 1', 'esta es la tarea 1', 'ALTA', d)
tareas.append(t)
t2 = Tarea('tarea 2', 'esta es la tarea 2', 'BAJA', p)
tareas.append(t2)
#guardar tareas en archivo

for tarea in tareas:
    tarea : Tarea
    if tarea.get_usuario().get_nombre() == d.get_nombre():
        print(tarea.get_info())