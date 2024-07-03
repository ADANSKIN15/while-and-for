# Convertir de decimal a binario: Pide al usuario un número entero positivo y convierte ese
# número a binario usando un ciclo while.

print('++++++++++++++++++++++++')
print('  Decimal a Binario')
print('++++++++++++++++++++++++\n')


num = int(input('Ingrese un número entero: '))

binario = bin(num)[2:]

print(f'En binario de {num} es : {binario}')