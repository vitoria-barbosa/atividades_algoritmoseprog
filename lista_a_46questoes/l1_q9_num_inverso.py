# 9. Leia 2 números (A, B) e escreva-os em ordem inversa (B, A).

# Entrada
num = int(input('Digite um número de 2 dígitos:'))

# Processamento
dez = num // 10
un = num % 10
inverso = (un * 10) + dez

# Saída
print(f'O inverso de {num} é {inverso}.')
