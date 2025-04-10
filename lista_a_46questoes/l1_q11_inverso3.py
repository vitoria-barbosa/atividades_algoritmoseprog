# 11. Leia um número inteiro (3 dígitos) e escreva o inverso do número.

# Entrada
num = int(input('Digite um número de 3 dígitos:'))

# Processamento
c = num // 100
d = (num % 100) // 10
u = (num % 100) % 10
inverso = (u * 100) + (d * 10) + c

# Saída
print(f'O inverso do número {num} é {inverso}!')
