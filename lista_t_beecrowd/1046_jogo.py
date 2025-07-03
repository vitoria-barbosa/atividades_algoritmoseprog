# Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, sabendo que o mesmo pode começar em um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24 horas.
def main():
    entrada = input("")
    hora_inicio = int(entrada.split()[0])
    hora_final = int(entrada.split()[1])
    duracao = validar_tempo(hora_inicio, hora_final)
    print(f"O JOGO DUROU {duracao} HORA(S)")


def validar_tempo(inicio, final):
   if final < inicio:
      return (24 - inicio) + final
   elif final == inicio:
      return 24
   else:
      return final - inicio
   

main()