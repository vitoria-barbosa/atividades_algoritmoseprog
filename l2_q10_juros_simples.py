# Escreva um programa que calcule o montante final em uma aplicação financeira com juros simples.

# Entrada
capital = float(input('Valor do capital a ser investido:'))
taxa = float(input('Taxa de juros a ser aplicada:'))
tempo = float(input('Tempo:'))

# Processamento
juros = capital * taxa * tempo
montante = juros + capital

# Saída
print(f'O montante final dessa aplicação financeira será de R$ {montante:.2f}')
