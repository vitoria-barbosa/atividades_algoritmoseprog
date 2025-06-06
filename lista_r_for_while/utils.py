def obter_num_int(label):
    entrada = input(label)

    try: 
        num = int(entrada)
        
        if num >= 0:
            return num
        else:
            print("Entrada inválida. Digite um número positivo.")
            return obter_num_int(label)
        
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")
        return obter_num_int(label)
    

def obter_num_float(label):
    entrada = input(label)

    try: 
        num = float(entrada)
        
        if num >= 0:
            return num
        else:
            print("Entrada inválida. Digite um número positivo.")
            return obter_num_float(label)
        
    except ValueError:
        print("Entrada inválida. Digite um número float.")
        return obter_num_float(label)