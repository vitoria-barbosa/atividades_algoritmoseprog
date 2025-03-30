# Escreva um programa que receba um número de três dígitos e exiba ele invertido.

# Entrada
num = int(input('Digite um número de 3 dígitos:'))

# Processamento
c = num // 100
d = (num % 100) // 10
u = (num % 100) % 10
inverso = (u * 100) + (d * 10) + c

# Saída
print(f'O inverso do número {num} é {inverso}.')
