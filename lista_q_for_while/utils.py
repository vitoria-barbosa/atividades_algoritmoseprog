def obter_num_int(label):
    entrada = input(label)
    
    try:
        num = int(entrada)

        if num >= 0:
            return num
        else: 
            print("Entrada inválida! Digite um número positivo.")
            return obter_num_int(label)

    except ValueError:
        print("Entrada inválida! Digite um número inteiro e positivo.")
        return obter_num_int(label)
    

def obter_num_int_faixa(label, min, max):
    entrada = input(label)
    
    try:
        num = int(entrada)

        if num >= min and num <= max:
            return num
        else: 
            print(f"Entrada inválida! Digite um número positivo e dentro da faixa {min} - {max}.")
            return obter_num_int(label)

    except ValueError:
        print("Entrada inválida! Digite um número inteiro e positivo.")
        return obter_num_int(label)
    

def obter_num_float(label):
    entrada = input(label)
    
    try:
        num = float(entrada)

        if num >= 0:
            return num
        else: 
            print("Entrada inválida! Digite um número positivo.")
            return obter_num_int(label)

    except ValueError:
        print("Entrada inválida! Digite um número float positivo.")
        return obter_num_int(label)