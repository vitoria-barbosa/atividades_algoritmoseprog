# Escreva um algoritmo que leia um número decimal (até 3 dígitos) e escreva o seu equivalente em
# numeração romana. Utilize funções para obter cada dígito do número decimal e para a transformação
# de numeração decimal para romana (Dica: 1 = I, 5 = V, 10 = X, 50 = L, 100 = C, 500 = D, 1.000 = M).
from utils import obter_num_int_faixa
def main():
    num = obter_num_int_faixa("Digite um número: ", 1, 999)
    romano = decimal_para_romano(num)

    print(f"{num} em romano é {romano}")


def obter_digitos(numero):
    centenas = numero // 100
    dezenas = (numero % 100) // 10
    unidades = numero % 10
    return centenas, dezenas, unidades

def decimal_para_romano(numero_decimal):

    centenas, dezenas, unidades = obter_digitos(numero_decimal)

    romano_centenas = decimal_para_romano_digito(centenas, 'C', 'D', 'M')
    romano_dezenas = decimal_para_romano_digito(dezenas, 'X', 'L', 'C')
    romano_unidades = decimal_para_romano_digito(unidades, 'I', 'V', 'X')

    return romano_centenas + romano_dezenas + romano_unidades


def decimal_para_romano_digito(digito, um, cinco, dez):
    # 'um', 'cinco', 'dez' são os caracteres romanos correspondentes a 1, 5 e 10 
    # para aquela casa (ex: para unidades, são 'I', 'V', 'X'; para dezenas, 'X', 'L', 'C').
    if digito == 0:
        return ""
    elif digito <= 3:
        return um * digito
    elif digito == 4:
        return um + cinco
    elif digito == 5:
        return cinco
    elif digito == 6:
        return cinco + um
    elif digito == 7:
        return cinco + (um * 2)
    elif digito == 8:
        return cinco + (um * 3)
    elif digito == 9:
        return um + dez
    else:
        return "" # Para qualquer outro caso (não deve ocorrer com dígitos de 0 a 9)

main()