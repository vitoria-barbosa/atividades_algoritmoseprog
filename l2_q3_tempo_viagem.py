# Escreva um programa que calcule quanto tempo levará uma viagem, dado a distância e a
# velocidade média.

# Entrada
distancia = float(input('Distância em km:'))
velocidade = int(input('Qual a velocidade média(Km/h):'))

# Processamento
tempo = distancia / velocidade

# Saída
print(f'A {velocidade} Km/h você chegará ao seu destino após {tempo} horas.')
