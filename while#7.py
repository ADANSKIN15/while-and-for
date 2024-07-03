# Validar entrada:
# Pide al usuario que ingrese un número positivo.
# Si el usuario ingresa un  número negativo,
# solicita nuevamente la entrada hasta que ingrese un número positivo. Usa  un ciclo while.

print('______________________________________________')
print('    identifica si es positivo o negativo')
print('        se detine solo si es positivo')
print('______________________________________________\n')

stop = 0
can = int(input('ingrese un numero: '))

print()

while stop == 0 :
    if can < 0 :
        print('el numero es negativo ')
        top = int(input('intentelo de nuevo: '))
        
        if top > 0 :
            print(f'el numero {top} es positivo')
            break
            
    
    
       
 

    
    
    
    
    