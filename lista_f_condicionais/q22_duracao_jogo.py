# Leia a hora do início de um jogo e a hora de fim do jogo (cada hora é composta por 2 variáveis inteiras:
# hora e minuto). Calcule e escreva a duração do jogo (horas e minutos), sabendo-se que o tempo
# máximo de duração do jogo é de 24 horas e que ele pode iniciar-se em um dia e terminar no dia seguinte.
from package.io_utils import obter_numero_inteiro

def main():
    print('Início do jogo: ')
    hora_inicio = obter_numero_inteiro('Hora: ')
    min_inicio = obter_numero_inteiro('Minutos: ')
    hora_final = obter_numero_inteiro('Hora: ')
    min_final = obter_numero_inteiro('Minutos: ')
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
    return print(f'A duração do jogo foi igual a {horas}h e {minutos}min')


def horas_to_minutos(horas, minutos):
   return horas * 60 + minutos

main()