# Simular un cajero automático: Escribe un programa que simule un cajero automático. Pide
# al usuario que ingrese su PIN y permite tres intentos para ingresarlo correctamente. Si no lo
# hace en tres intentos, muestra un mensaje de bloqueo. Usa un ciclo while.

print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
print('$       cajero automático        $ ')
print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n')

print('solo tiene 3 intentos')
stop = 0

while stop < 3 :
    can = int(input('ingrese pin: '))
    stop += 1
    
    if can != 1234 :
        print('incorrecto')
        print('intento',stop)
    
    if can == 1234 :
        print('correcto')
        break
    
    if stop == 3:
        print('cuenta bloqueada')
        

        