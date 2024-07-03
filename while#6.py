# Mostrar múltiplos de un número:
# Pide al usuario un número entero positivo
# y muestra sus  múltiplos del 1 al 10 usando un ciclo while.

print('**************************')
print('    Vamos a multiplicar   ')
print('**************************\n')

mul = int(input('Ingrese el número que desea multiplicar hasta 10: '))

s = 0

while s < 10:
    s += 1
    t = mul * s
    print(f'{mul} * {s} = {t}')


    
    
    