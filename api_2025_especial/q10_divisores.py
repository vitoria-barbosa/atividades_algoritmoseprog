# Receba dois valores inteiro A e B positivos com
# B > A em pelo menos 11 unidades. Em seguida, mostre todos os
# valores de A até B, e coloque ao lado a quantidade de divisores
# desse número.
# começo: 10:15 fim: 11:10
from q1_number_utils import obter_numero_int_positivo, obter_numero_int_min

def main():
    a = obter_numero_int_positivo("Digite um valor para A: ")
    b = obter_numero_int_min("Digite um valor para B: ", a + 11)
    contador = b - a
    num = a

    while contador >= 0:
        divisores = calcular_divisores(num)
        print(f"{num}  ({divisores} divisores)")
        num += 1
        contador -= 1

def calcular_divisores(n):
    qtd_divisores = 0
    divisor = n

    while divisor > 0:
        if n % divisor == 0:
            qtd_divisores += 1
        divisor -= 1
    
    return qtd_divisores

main()