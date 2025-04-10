# 33. Leia um número inteiro (3 dígitos), calcule e escreva a soma do número com seu inverso.

def principal():
    num = int(input('Digite um número inteiro de 3 dígitos: '))
    c = num // 100
    d = (num % 100) // 10
    u = (num % 100) % 10
    inverso = u * 100 + d * 10 + c
    soma = num + inverso

    print(f'A soma entre o número {num} e seu inverso {inverso} é igual a = {soma}')

principal()
