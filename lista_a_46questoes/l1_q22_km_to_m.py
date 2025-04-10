# Leia um valor em km, calcule e escreva o equivalente em m.

def principal():
    km = float(input('Digite um valor em Km: '))
    metros = km * 1000

    print(f'>>> {km} km equivalem a {metros:.0f} metros.')

principal()
