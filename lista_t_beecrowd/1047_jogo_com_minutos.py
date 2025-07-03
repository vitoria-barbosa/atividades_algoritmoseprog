def main():
    entrada = input("")
    hora_inicio = int(entrada.split()[0])
    min_inicio = int(entrada.split()[1])
    hora_final = int(entrada.split()[2])
    min_final = int(entrada.split()[3])
    inicio_total_min = horas_to_minutos(hora_inicio, min_inicio)
    final_total_min = horas_to_minutos(hora_final, min_final)
    duracao_min = validar_tempo(inicio_total_min, final_total_min)
    minutos_to_horasemin(duracao_min)


def validar_tempo(inicio_total_min, final_total_min):
   if final_total_min < inicio_total_min:
      return (24 * 60 - inicio_total_min) + final_total_min
   elif final_total_min == inicio_total_min:
      return 24 * 60
   else:
      return final_total_min - inicio_total_min


def minutos_to_horasemin(duracao_min):
    horas = duracao_min // 60 
    minutos = duracao_min % 60 
    return print(f'O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)')


def horas_to_minutos(horas, minutos):
   return horas * 60 + minutos

main()