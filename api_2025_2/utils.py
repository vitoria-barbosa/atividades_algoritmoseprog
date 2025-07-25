def obter_num_int(label):
    entrada = input(label)

    try:
        num = int(entrada)
        return num

    except ValueError:
        print("Entrada inválida. Digite um número inteiro: ")
        return obter_num_int(label)


def obter_num_float(label):
    entrada = input(label)

    try:
        num = float(entrada)
        return num

    except ValueError:
        print("Entrada inválida. Digite um número float: ")
        return obter_num_float(label)


def obter_num_em_faixa(label, min, max):
    num = int(input(label))

    if min <= num <= max:
        return num
    else:
        print(f"Número fora da faixa. Escreva um número entre {min} e {max}:")
        return obter_num_em_faixa(label, min, max)