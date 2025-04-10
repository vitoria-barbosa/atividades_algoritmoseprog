# Leia um número inteiro de metros, calcule e escreva quantos Km e quantos metros ele corresponde.

def principal():
    metros = int(input('Digite uma quantidade de metros: '))
    km = metros // 1000
    metros_restantes = metros % 1000

    print(f'{metros} metros correspondem a {km} quilômetros e {metros_restantes} metros.')

principal()
