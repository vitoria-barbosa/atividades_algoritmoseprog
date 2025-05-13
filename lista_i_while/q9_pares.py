from package.io_utils import obter_numero_inteiro

def main():
    print('---- NÚMEROS PARES----')
    limite_inferior = obter_numero_inteiro('Limite Inferior: ')
    limite_superior = obter_numero_inteiro('Limite Superior: ')
    print(f'\nEntre {limite_inferior} e {limite_superior} esses são os números pares:')
    escrever_multiplos(limite_inferior, limite_superior)


def escrever_multiplos(limite_inf, limite_sup):
        candidato = limite_inf
        while candidato <= limite_sup:
            if candidato % 2 == 0:
                print(candidato)
            candidato += 1

main()