# 35. Leia um número inteiro (4 dígitos), calcule e escreva a soma dos elementos que o compõem.

def principal():
    num = int(input('Digite um número inteiro de 4 dígitos: '))
    m = num // 1000
    c = (num % 1000) // 100
    d = ((num % 1000) % 100) // 10
    u = ((num % 1000) % 100) % 10
    soma = m + c + d + u

    print(f'A soma dos elementos desse número, ou seja, {m} + {c} + {d} + {u} é igual a = {soma}')

principal()
