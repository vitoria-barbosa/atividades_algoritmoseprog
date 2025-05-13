# Leia N , LimiteSuperior e LimiteInferior e escreva todos os múltiplos de N entre os limites lidos.
from package.io_utils import obter_numero_inteiro
def main():
    n = obter_numero_inteiro('Digite um número:  ')
    limite_inferior = obter_numero_inteiro('Limite Inferior: ')
    limite_superior = obter_numero_inteiro('Limite Superior: ')
    escrever_multiplos(n, limite_inferior, limite_superior)
    print(f'Entre {limite_inferior} e {limite_superior} esses são os múltiplos de {n}')


def escrever_multiplos(n, limite_inf, limite_sup):
        candidato = limite_inf
        while candidato <= limite_sup:
            if candidato % n == 0:
                print(candidato)
            candidato += 1

main()