# 27. Leia um número inteiro de segundos, calcule e escreva quantas horas, quantos minutos e quantos segundos ele corresponde.

def principal():
    segundos = int(input('Digite uma quantidade de segundos: '))
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos_restantes = (segundos % 3600) % 60

    print(f'>>> {segundos} segundos correspondem a {horas} hora(s), {minutos} minutos(s) e {segundos_restantes} segundos(s).')

principal()
