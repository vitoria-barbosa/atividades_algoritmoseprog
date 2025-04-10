# 41. O custo ao consumidor de um carro novo é a soma do custo de fábrica com a percentagem do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que a percentagem do distribuidor seja de 28% e os impostos de 45%, escreva um algoritmo que leia o custo de fábrica de um carro e escreva o custo ao consumidor.

def principal():
    custo_de_fabrica = float(input('Valor do custo de fábrica do carro: '))
    porcentagem_distribuidor = calcular_porcentagem(custo_de_fabrica,28)
    impostos = calcular_porcentagem(custo_de_fabrica,45)
    custo_total = custo_de_fabrica + porcentagem_distribuidor + impostos

    print(f'\nO carro com custo de fabrica de R${custo_de_fabrica:.2f}, ao somar a porcentagem do distribuidor de 24% que é R${porcentagem_distribuidor:.2f} e os impostos de 45% que dá R${impostos:.2f} fica custando no total R${custo_total:.2f}')


def calcular_porcentagem(custo,porcentagem):
    return (porcentagem / 100) * custo

principal()    
