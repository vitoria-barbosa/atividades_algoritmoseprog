# Escreva um programa que determine a quantidade de notas de 50 e 10 necessárias para um
# determinado valor.

# Entrada
valor = int(input('Digite um valor inteiro:'))

# Processamento
notas_50 = valor // 50
notas_10 = (valor % 50) // 10

# Saída
print(f'{valor} reais correspondem a {notas_50} nota(s) de 50 reais e {notas_10} nota(s) de 10 reais.')
