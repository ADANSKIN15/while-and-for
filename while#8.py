# Contador de dígitos: Pide al usuario un número entero y cuenta cuántos dígitos tiene usando
# un ciclo while.

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
print('       contador de dígitos           ')
print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n')

def digito(a) :
    x = 0
    while a > 0 :
        x += 1
        a //= 10
        
    return x


    
val = int(input('introdusca un numero entero: '))

print()

print(f'el numero {val} tiene {digito(val)} digitos')
        
    