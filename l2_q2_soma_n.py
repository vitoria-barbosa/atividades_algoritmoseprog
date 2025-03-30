# Escreva um programa que calcule a soma dos primeiros N números naturais.
# Ex:5 >> 1+2+3+4+5= 15
# Entrada
num = int(input('Digite um número:'))

# Processamento
soma = num * (num + 1) / 2

# Saída
print(f'A soma de todos o números naturais até o {num} é = {soma}!')
