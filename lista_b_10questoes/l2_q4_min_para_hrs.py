# Escreva um programa que converta minutos para horas e minutos.

# Entrada
minutos = int(input('Digite uma quantidade de minutos: '))

# Processamento
horas = minutos // 60
min = minutos % 60

# Saída
print(f'{minutos} minutos correspondem a {horas} hora(s) e {min} minutos.')
