# Imprimir números impares:
# Pide al usuario un número entero positivo y muestra todos los  números impares
# del 1 hasta ese número usando un ciclo for.

print('________________________________________________')
print('  Imprimir números impares, hasta un limite')
print('________________________________________________\n')

can = int(input("Ingrese un número límite: "))
print()

for i in range(1, can + 1, 2):
    print(i)
        
    
