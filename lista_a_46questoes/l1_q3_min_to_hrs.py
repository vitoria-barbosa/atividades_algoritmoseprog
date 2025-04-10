# 3. Leia um valor em minutos, calcule e escreva o equivalente em horas e minutos.

# Entrada
minutos = int(input('Digite uma quantidade de minutos: '))

# Processamento
horas = minutos // 60
min = minutos % 60

# Saída
print(f'{minutos} minutos correspondem a {horas}h{min}min.')
