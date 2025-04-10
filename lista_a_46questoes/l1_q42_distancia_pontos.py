# Escreva um algoritmo que, tendo como dados de entrada 2 pontos quaisquer no plano, ponto1 (x1,y1) e ponto2 (x2,y2), escreva a distância entre eles

import math

def principal():
    print('> 1° ponto do plano:')
    x1 = int(input('x: '))
    y1 = int(input('y: '))
    print('> 2° ponto do plano:')
    x2 = int(input('x: '))
    y2 = int(input('y: '))

    soma = ((x2 - x1)**2) + ((y2 - y1)**2)
    distancia = math.sqrt(soma)

    print(f'\nA distância entre os pontos ({x1},{y1}) e ({x2},{y2}) no plano é aproximadamente {distancia:.2f} unidades')


principal()
