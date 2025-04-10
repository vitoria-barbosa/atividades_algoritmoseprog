# 29. Leia um número inteiro de meses, calcule e escreva quantos anos e quantos meses ele corresponde.

def principal():
    meses = int(input('Digite uma quantidade de meses: '))
    anos = meses // 12
    meses_restantes = meses % 12

    print(f'>>> {meses} meses correspondem a {anos} ano(s) e {meses_restantes} mês(es).')

principal()
