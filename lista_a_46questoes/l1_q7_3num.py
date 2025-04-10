# Leia 3 números, calcule e escreva a soma dos 2 primeiros e a diferença entre os 2 últimos.

# Entrada
n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))
n3 = int(input('Digite mais um número:'))

# Processamento
soma = n1 + n2
diferenca = n2 - n3

# Saída
print(f'A soma de {n1} e {n2} é {soma}, enquanto a diferença entre {n2} e {n3} é {diferenca}.')
