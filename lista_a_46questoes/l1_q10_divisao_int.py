# 10. Leia 2 números inteiros, calcule e escreva o quociente e o resto da divisão do 1° pelo 2°

# Entrada
n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))

# Processamento
divisao = n1 // n2
resto = n1 % n2

# Saída
print(f'Na divisão entre esses dois números, {divisao} é o quociente e {resto} é o resto.')
