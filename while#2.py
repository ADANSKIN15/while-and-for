# Contar hasta un número dado:
# Pide al usuario un número entero positivo y muestra todos  los números
# del 1 hasta ese número usando un ciclo while.

print('--------------------------------------')
print('     Contar hasta un número dado      ')
print('--------------------------------------\n ')

con = int(input('ingrese un numero entero: '))
cont = 0

print()

while cont < con :
    cont += 1
    print(cont)
    