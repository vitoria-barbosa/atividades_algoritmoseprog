# 28. Leia um número inteiro de horas, calcule e escreva quantas semanas, quantos dias e quantas horas ele corresponde.

def principal():
    horas = int(input('Digite uma quantidade de horas: '))
    semanas = horas // 168
    dias = (horas % 168) // 24
    horas_restantes = (horas % 168) % 24

    print(f'>>> {horas} horas correspondem a {semanas} semana(s), {dias} dia(s) e {horas_restantes} hora(s).')

principal()
