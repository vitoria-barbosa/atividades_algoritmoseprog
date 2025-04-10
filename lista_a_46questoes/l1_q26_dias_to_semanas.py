# 26. Leia um número inteiro de dias, calcule e escreva quantas semanas e quantos dias ele corresponde.

def principal():
    dias = int(input('Digite uma quantidade de dias: '))
    semanas = dias // 7
    dias_restantes = dias % 7

    print(f'>>> {dias} dias correspondem a {semanas} semana(s) e {dias_restantes} dia(s).')

principal()
