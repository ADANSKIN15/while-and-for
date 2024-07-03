# Sumar números hasta un límite:
# Pide al usuario que ingrese números enteros positivos uno  a uno
# y suma estos números hasta que la suma alcance un límite (por ejemplo, 100).
# Usa un  ciclo while.

print('---------------------------------')
print('| Sumar números hasta un límite | ')
print('--------------------------------- \n ')

cont = 0

while cont < 100 :
    cont += int(input('ingrese un numero: '))
    print('el numero va en ',cont)
    
print()
          
print(f'te pasaste por :{cont - 100}')            
    
      