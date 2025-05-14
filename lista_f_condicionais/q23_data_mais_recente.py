# Leia 2 datas (cada data é composta por 3 variáveis inteiras: dia, mês e ano) e escreva qual delas é a mais recente.
from package.io_utils import obter_numero_inteiro
from q10_data_valida import obter_dia_valido
from q10_data_valida import obter_mes_valido
from q10_data_valida import obter_ano_valido

def main():
    print('Data 1: ')
    data1_dia = obter_dia_valido()
    data1_mes = obter_mes_valido()
    data1_ano = obter_ano_valido()
    data1 = f'{data1_dia}/{data1_mes}/{data1_ano}'
    print('Data 2: ')
    data2_dia = obter_dia_valido()
    data2_mes = obter_mes_valido()
    data2_ano = obter_ano_valido()
    data2 = f'{data2_dia}/{data2_mes}/{data2_ano}'
    maior_data = ''

    if data1_ano > data2_ano:
        maior_data = data1
    elif data2_ano > data1_ano:
        maior_data = data2
    elif data1_mes > data2_mes:
        maior_data = data1
    elif data2_mes > data1_mes:
        maior_data = data2
    elif data1_dia > data2_dia:
        maior_data = data1
    else:
        maior_data = data2

    print(f'\n{maior_data} é mais recente.')

main()