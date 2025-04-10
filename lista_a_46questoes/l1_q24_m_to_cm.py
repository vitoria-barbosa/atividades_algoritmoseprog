# Leia um valor em m, calcule e escreva o equivalente em cm.

def principal():
    metros = float(input('Digite um valor em metros: '))
    cm = metros * 100

    print(f'>>> {metros} metro(s) equivale(m) a {cm:.0f} centímetros.')

principal()
