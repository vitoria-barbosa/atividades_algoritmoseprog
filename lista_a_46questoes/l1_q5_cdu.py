# 5. Leia um número inteiro (3 dígitos), calcule e escreva a soma de seus elementos (C + D + U).

# Entrada
num = int(input('Digite um número de 3 dígitos: '))

# Processamento
centena = num // 100
dez = (num % 100) // 10
un = (num % 100) % 10
soma = centena + dez + un

# Saída
print(f'A soma dos elementos do número {num} é {soma}.')
