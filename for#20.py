# Repetir una cadena: Pide al usuario una cadena de texto y un número entero positivo NNN.
# Muestra la cadena repetida NNN veces, cada vez en una nueva línea, usando un ciclo for.\

texto = str(input('escriba un texto: '))
num = int(input('ingrese la cantidad de repeticiones: '))
import time
for i in range(1,num +1,1):
    print(texto, )
    time.sleep(1)