def obter_numero_float_positivo(label):
    entrada = (input(label))
    try:
        numero = float(entrada)
        if numero > 0:
            return numero
        else:
            print('0 e valores negativos não são válidos. Tente novamente: ')
            return obter_numero_float_positivo(label)
    except ValueError:
        print('Esse não é um valor válido. Tente novamente: ')
        return obter_numero_float_positivo(label)
    

def obter_numero_inteiro_positivo(label):
    entrada = (input(label))
    try:
        numero = int(entrada)
        if numero > 0:
            return numero
        else:
            print('0 e valores negativos não são válidos. Tente novamente: ')
            return obter_numero_inteiro_positivo(label)
    except ValueError:
        print('Esse não é um valor válido. Tente novamente: ')
        return obter_numero_inteiro_positivo(label)