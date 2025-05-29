# Leia N e uma lista de N números e escreva o maior número da lista.
from utils import obter_num_inteiro

def main():
    qtd = obter_num_inteiro('Digite a quantidade de números: ')
    maior = 0

    for i in range(0, qtd, 1):
        num = obter_num_inteiro("Número: ")
        if num > maior:
            maior = num
    
    print(f'\nMaior número: {maior}')

main()