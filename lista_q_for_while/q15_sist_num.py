# Leia um número (entre 0 e 255) na base decimal, calcule e escreva este número na base binária
# e na base hexadecimal.
from utils import obter_num_int
def main():
    n = obter_num_int("Digite um número na base decimal: ")
    binario = em_binario(n)
    hexadecimal = em_hexadecimal(n)

    print(f"{n} em binario: {binario} e em hexadecimal: {hexadecimal}")

def em_binario(n):
    binario_invertido = " "

    while n > 1:
        divisao = n // 2
        resto = n % 2
        if divisao == 1:
            binario_invertido += f"{resto}{divisao}"
        else:
            binario_invertido += f"{resto}"
        n = divisao
        binario = binario_invertido[::-1]
    return binario


def em_hexadecimal(n):
    hexadecimal_invertido = " "

    while n > 1:
        divisao = n // 16
        resto = n % 16
        if resto == 10:
            resto = "A"
        if resto == 11:
            resto = "B"
        if resto == 12:
            resto = "C"
        if resto == 13:
            resto = "D"
        if resto == 14:
            resto = "E"
        if resto == 15:
            resto = "F"
        if divisao == 1:
            hexadecimal_invertido += f"{resto}{divisao}"
        else:
            hexadecimal_invertido += f"{resto}"
        n = divisao
        hexadecimal = hexadecimal_invertido[::-1]
    return hexadecimal


main()