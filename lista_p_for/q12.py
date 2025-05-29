# Leia N e uma lista de N números e escreva a soma e a média de todos os números da lista.
from utils import obter_num_inteiro

def main():
    qtd = obter_num_inteiro('Digite a quantidade de números: ')
    somatorio = 0

    for i in range(0, qtd, 1):
        num = obter_num_inteiro('Número: ')
        somatorio += num

    media = somatorio / qtd

    print(f'\nSoma = {somatorio}, Média = {media:.1f}')

main()