nombre = 'Cristian'
apellido = 'Briones'
numeroTelefonico = 7224171471

file = open('agenda','a')
file.write(f'{nombre},{apellido},{numeroTelefonico}')
file.close