# Leia N , LimiteSuperior e LimiteInferior e escreva todos os múltiplos de N entre os limites lidos.
from utils import obter_num_inteiro
def main():
    n = obter_num_inteiro('Digite um número:  ')
    limite_inferior = obter_num_inteiro('Limite Inferior: ')
    limite_superior = obter_num_inteiro('Limite Superior: ')
    print(f'Entre {limite_inferior} e {limite_superior} esses são os múltiplos de {n}:')

    for i in range(limite_inferior, limite_superior+1, 1):
        if i % n == 0:
            print(i)

main()