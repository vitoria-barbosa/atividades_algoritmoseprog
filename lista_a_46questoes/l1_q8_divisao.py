# 8. Leia 2 números, calcule e escreva a divisão da soma pela subtração dos números lidos.

# Entrada
n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))

# Processamento
divisao = (n1 + n2) / (n1 - n2)

# Saída
print(f'A divisão da soma entre {n1} e {n2} pela diferença entre eles é = {divisao:.1f}.')

