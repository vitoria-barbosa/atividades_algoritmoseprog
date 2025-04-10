# Escreva um algoritmo que receba o valor da quantia solicitada e retorne a distribuição das notas de acordo com o critério da distribuição ótima.

def principal():
    quantia = int(input('Digite uma quantia inteira em R$: '))
    notas_50 = quantia // 50
    notas_10 = (quantia % 50) // 10
    notas_5 = ((quantia % 50) % 10) // 5
    notas_1 = ((quantia % 50) % 10) % 5

    print(f'Para a quantia de R${quantia} você receberá {notas_50} nota(s) de R$50, {notas_10} nota(s) de R$10, {notas_5} nota(s) de R$5 e {notas_1} nota(s) de R$1.')

principal()
