# Sumar dígitos de un número:
# Pide al usuario un número entero y suma sus dígitos usando  un ciclo while.

print('==============================')
print('  Sumar dígitos de un número  ')
print('============================== \n')


F = int(input('ingrese un numero: '))

suma = 0

print()

while F > 0 :
    suma += (F % 10)
    F //= 10
    
print(f'la suma de sus digitos es:{suma}')