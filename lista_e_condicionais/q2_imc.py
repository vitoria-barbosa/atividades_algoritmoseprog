# Calculadora de IMC com Classificação
import sys
sys.path.append('C:\\Users\\vitor\\algoritmos_e_prog\\lista_f_condicionais')
from package.io_utils import obter_numero_float

def main():
    print('\n------CALCULAR IMC------')
    peso = obter_numero_float('Peso(Kg): ')
    altura = obter_altura('Altura(m): ')
    imc = calcular_imc(peso,altura)
    classificacao = classificar_imc(imc)

    print(f'\nSeu IMC é {imc:.2f} e é classificado como {classificacao}')


def calcular_imc(peso, altura):
  return peso / (altura**2)


def classificar_imc(imc):
    if imc < 18.5:
       return 'Abaixo do peso'
    elif imc < 24.9:
       return 'Peso normal'
    elif imc < 29.9:
       return 'Sobrepeso'
    elif imc < 34.9:
       return 'Obesidade grau 1'
    elif imc < 39.9:
       return 'Obesidade grau 2'
    else:
       return 'Obesidade grau 3'
    

def obter_altura(label: str):
    altura = float(input(label))
    if 1.00 < altura < 2.50:
       return altura
    else:
       print(f'{altura} não é uma altura válida. Tente novamente')
       return obter_altura(label)

main()