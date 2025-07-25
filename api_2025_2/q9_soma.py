import utils as u

def main():
    primeiro_numero = u.obter_num_em_faixa("Número: ", 1, 99)
    somatorio_multiplos = primeiro_numero
    numero = u.obter_num_em_faixa("Número: ", 1, 99)

    while numero != primeiro_numero:

        if numero % primeiro_numero == 0:
            somatorio_multiplos += numero

        numero = u.obter_num_em_faixa("Número: ", 1, 99)

    somatorio_multiplos += numero


    print(f"\nSomatório de todos os múltiplos de {primeiro_numero}, incluindo ele: {somatorio_multiplos}")


main()