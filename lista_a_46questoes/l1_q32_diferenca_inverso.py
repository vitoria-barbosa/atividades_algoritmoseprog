# 32. Leia um número inteiro (3 dígitos), calcule e escreva a diferença entre o número e seu inverso.

def principal():
    num = int(input('Digite um número inteiro de 3 dígitos: '))
    c = num // 100
    d = (num % 100) // 10
    u = (num % 100) % 10
    inverso = u * 100 + d * 10 + c
    diferenca = num - inverso

    print(f'A diferença entre o número {num} e seu inverso {inverso} é igual a = {diferenca}')

principal()
