from package.io_utils import obter_numero_inteiro

def main():
    print('---- NÚMEROS PRIMOS----')
    limite_inferior = obter_numero_inteiro('Limite Inferior: ')
    limite_superior = obter_numero_inteiro('Limite Superior: ')
    print(f'\nEntre {limite_inferior} e {limite_superior} esses são os números primos:')
    escrever_primos(limite_inferior, limite_superior)
    print('Fim.')


def escrever_primos(limite_inf, limite_sup):
    candidato = limite_inf
    while candidato <= limite_sup:
        eh_primo(candidato)
        candidato += 1
                 

def eh_primo(n):
    if n <= 1:
         return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
             return False
    return print(n)

main()