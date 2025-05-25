# Escreva um programa que pede o nome de usuário
# e então a partir do tamanho do nome faça o seguinte. Se o nome
# tiver tamanho T ímpar, mostrar todos os divisores até 1. Se o
# tamanho T for par mostrar os próximos T múltiplos de T.
from q2_int_utils import obter_numero_int_positivo
def main():
    nome = input("Digite um nome: ")
    tamanho = len(nome)

    if tamanho % 2 == 0: #par
        contador = tamanho
        multiplo = tamanho
        while contador > 0:
            multiplo += tamanho
            print(multiplo)
            contador -= 1
    else:   #ímpar
        divisor = tamanho
        while divisor > 0:
           if tamanho % divisor == 0:
               print(divisor)
           divisor -= 1 

            


main()