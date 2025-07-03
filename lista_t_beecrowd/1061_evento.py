# Como entrada, na primeira linha vai haver a descrição “Dia”, seguido de um espaço e o dia do mês no qual o evento vai começar. Na linha seguinte, será informado o momento no qual o evento vai iniciar, no formato hh : mm : ss. Na terceira e quarta linha de entrada haverá outra informação no mesmo formato das duas primeiras linhas, indicando o término do evento.
# Na saída, deve ser apresentada a duração do evento, no seguinte formato:
# W dia(s)
# X hora(s)
# Y minuto(s)
# Z segundo(s)
def main():
    entrada1 = input("")
    dia_inicio = int(entrada1.split()[1])
    hora_inicio , minuto_inicio, segundo_inicio = map(int, input("").split(" : "))
    entrada2 = input("")
    dia_termino = int(entrada2.split()[1])
    hora_fim , minuto_fim, segundo_fim = map(int, input("").split(" : "))

    dia_inicio_em_seg = dia_inicio * 86400 + hora_inicio * 3600 + minuto_inicio * 60 + segundo_inicio
    dia_fim_em_seg = dia_termino * 86400 + hora_fim * 3600 + minuto_fim * 60 + segundo_fim
    duracao = dia_fim_em_seg - dia_inicio_em_seg

    dias = duracao // 86400
    horas_restantes = duracao % 86400
    horas  = horas_restantes // 3600
    minutos_restantes = horas_restantes % 3600
    minutos  = minutos_restantes // 60
    segundos = minutos_restantes % 60

    print(f"{dias} dia(s)")
    print(f"{horas} hora(s)")
    print(f"{minutos} minuto(s)")
    print(f"{segundos} segundo(s)")


main()