# Tabla de multiplicar:
# Pide al usuario un número entero positivo y muestra su tabla de
# multiplicar del 1 al 10 usando un ciclo for.

print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
print('        TABLAS DE MULTIPLICAR       ')
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n')

can = int(input('tabla de multiplicar de: '))
print()

for x in range(1,11) :
    mul = x * can
    print(can,'X',x,'=',mul)