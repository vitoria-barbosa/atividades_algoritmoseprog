# Leia uma data (dia, mês e ano), verifique e escreva se a data é ou não válida.

def main():
    print('Digite uma data:\n')
    
    dia_valido = obter_dia_valido()
    mes_valido = obter_mes_valido()
    ano_valido = obter_ano_valido()
    print(f'A data {dia_valido}/{mes_valido}/{ano_valido} é válida!')


def obter_dia_valido():
    dia = int(input('Dia: '))
    if 1 <= dia <= 31:
        return dia
    else:
        print(f'{dia} não é valido. Digite um dia entre 1 e 31.')
        return obter_dia_valido()


def obter_mes_valido():
    mes = int(input('Mês: '))
    if 1 <= mes <= 12:
        return mes
    else:
        print(f'{mes} não é valido. Digite um valor entre 1 e 12.')
        return obter_mes_valido()


def obter_ano_valido():
    ano = int(input('Ano: '))
    if ano / 1000 >= 1 and ano / 1000 < 10:
        return ano
    else:
        print(f'{ano} não é valido. Digite um ano de 4 dígitos.')
        return obter_ano_valido()

main()