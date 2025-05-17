# De acordo com a OMS, um homem adulto em média precisa
# consumir apenas 2400 calorias/dia para manter o peso atual. Já
# as mulheres ficam em 2000 calorias. Ou seja, esse é o valor que
# gastamos em atividades do dia a dia, normais. Já para perder 1kg
# de peso é necessário o gasto calórico excedente de 7000 calorias.
# Na academia, temos uma série de exercícios do tipo aeróbico,
# dentre eles o Transport e Simulador de Escada. No Transport, um
# homem gasta em média 100 calorias a cada 5 min, já uma mulher
# a cada 6 min. E na escada, um homem gasta 100 calorias a cada
# 7 minutos e a mulher a cada 8 minutos
# Faça um programa para auxiliar na perda de peso de homens e
# mulheres adultos. O objetivo é, de acordo com a situação atual
# (peso atual, se homem ou mulher, quantos quilos quer perder,
# quantos dias por semana irá fazer atividade física, e quanto tempo
# por dia irá treinar). Pergunte ainda qual proporção (%) de tempo
# alocada para o Transport, e calcule a contrapartida de Escada (os
# dois serão 100%).
# Seu objetivo, ao final, é informar em quantas semanas o usuário
# alcançará o objeto desejado, bem como indicar para cada dia de
# atividade física, quantos minutos de escada e quantos de
# Transport ele deverá seguir (todos os dias são iguais). Faça as
# validações adequadas.
def main():
    print('======== PLANO PARA EMAGRECER ========')
    # entrada
    peso_atual = float(input('Seu peso atual: '))
    sexo = int(input('Sexo(0 - Homem | 1 - Mulher): '))
    meta_quilos = float(input('Quantos quilos quer eliminar: '))
    dias_semana = int(input('Quantos dias por semana faz atividade física: '))
    horas_dia = float(input('Faz quantas horas de cardio por dia: '))
    porcentagem_transport = int(input('Proporção de tempo (%) que dedicará ao Transport: '))
    horas_transport = (horas_dia * (porcentagem_transport / 100))
    min_transport = horas_transport * 60
    horas_escada = horas_dia - horas_transport
    min_escada = horas_escada * 60
    meta_calorias_total = meta_quilos * 7000
    calorias_dia = calcular_calorias(sexo, min_transport, min_escada)
    semanas_total = ((meta_calorias_total / calorias_dia) / dias_semana)

    print(f'Fazendo Transport por {min_transport:.0f} minutos e escada por {min_escada:.0f} minutos por dia, você demorará {semanas_total:.1f} semanas para alcançar seu objetivo!')


def calcular_calorias(sexo, min_transport, min_escada):
    if sexo == 0:
        calorias_dia = (min_transport / 5 * 100) + (min_escada / 7 * 100)
        return calorias_dia
    else:
        calorias_dia = (min_transport / 6 * 100) + (min_escada / 8 * 100)
        return calorias_dia
    
main()