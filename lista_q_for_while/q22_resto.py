# Leia 2 números inteiros e escreva o quociente e o resto da divisão dos mesmos, sem que os operadores
# de divisão (/ e %) sejam utilizados.
from utils import obter_num_int
def main():
    n = obter_num_int("Digite um número: ")
    m = obter_num_int(f"Digite um número para dividir {n}: ")
    divisao = 0
    n_constante = n

    while n >= m:
        n -= m
        divisao += 1

    resto =  n_constante - (divisao * m) 

    print(f"Quociente: {divisao}, Resto: {resto}")

main()