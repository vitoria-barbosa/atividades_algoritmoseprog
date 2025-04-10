# 34. Leia 3 números, calcule e escreva a média dos números.

def principal():
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
    n3 = int(input('Digite mais um número: '))

    media = (n1 + n2 + n3) / 3

    print(f'A média entre os números {n1},{n2} e {n3} é igual a {media:.1f}')

principal()
