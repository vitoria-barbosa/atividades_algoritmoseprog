# Leia um número inteiro de minutos, calcule e escreva quantos dias, quantas horas e quantos minutos ele
#corresponde.

def principal():
    minutos = int(input('Digite uma quantidade de minutos:'))

    print(calcular_dias(minutos))



def calcular_dias(minutos):
    dias = minutos // 1440
    horas = (minutos % 1440) // 60
    minutos_restantes =  (minutos % 1440) % 60
    saida = f"{minutos} minutos correspondem a {dias} dias, {horas} horas e  {minutos_restantes} minutos"

    return saida

principal()
