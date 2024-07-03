# Convertir grados Celsius a Fahrenheit:
# Pide al usuario un rango de temperaturas en grados Celsius (inicio y fin)
# y muestra la conversión a Fahrenheit para cada grado en ese rango  usando un ciclo for.

print('**************************************')
print('Convertir grados Celsius a Fahrenheit ')
print('**************************************\n')


inicio = int(input(" inicio del rango en grados Celsius: "))
fin = int(input(" fin del rango en grados Celsius: "))


print(f"Conversión de grados Celsius a Fahrenheit para el rango de {inicio} a {fin} grados Celsius\n")


for celsius in range(inicio, fin + 1):
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius} grados Celsius son equivalentes a {fahrenheit:.2f} grados Fahrenheit")

print("FIN")


