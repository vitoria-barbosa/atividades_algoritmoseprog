# 31. Leia um número inteiro (4 dígitos binários), calcule e escreva o equivalente na base decimal.

def principal():
    binario = input('Digite um número binário de 4 dígitos(nibble): ')
    
    print(binario_para_decimal(binario))


def binario_para_decimal(binario):
    digitos = [int(d) for d in binario]
    decimal = digitos[0] * 8 + digitos[1] * 4 + digitos[2] * 2 + digitos[3] * 1 
    return decimal


principal()
