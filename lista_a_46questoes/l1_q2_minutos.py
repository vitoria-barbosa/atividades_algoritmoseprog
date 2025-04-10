# 2. Leia um valor em horas e um valor em minutos, calcule e escreva o equivalente em minutos.

# Entrada
horas = int(input('Digite uma quantidade de horas: '))
minutos = int(input('Digite uma quantidade de minutos: '))

# Processamento
soma = (horas * 60) + minutos

# Saída
print(f'{horas} horas e {minutos} minutos correspondem a {soma} minutos no total.')
