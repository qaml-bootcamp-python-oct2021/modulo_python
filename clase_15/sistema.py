from tarea import Tarea
from usuario import Usuario


usuarios = []

d = Usuario('David','david@mail.com')
usuarios.append(d)
#guardar usuarios en archivo

p = Usuario('Pepito','pepito@mail.com')
usuarios.append(p)

t = Tarea('Tarea 1','Esta es la tarea 1','ALTA')
c = Usuario('Clara','clara@mail.com')
c.set_tarea(t)
usuarios.append(c)


# guardar tareas en archivo

# for tarea in tareas:
#     tarea : Tarea
#     if tarea.get_usuario().get_nombre() == 'Clara':
#         print(tarea.get_info())

for usuario in usuarios:

    if usuario.get_nombre() == 'Clara':
        tareas = usuario.get_tareas()
        for tarea in tareas:
            tarea : Tarea
            print(tarea.get_info())

print(c.get_nombre())