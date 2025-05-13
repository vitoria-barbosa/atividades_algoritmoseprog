# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe
# contrataram para desenvolver o programa que calculará os reajustes. Escreva um algoritmo que leia o
# salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# o salários até R$ 280,00 (incluindo) : aumento de 20%
# o salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# o salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# o salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# · o salário antes do reajuste;
# · o percentual de aumento aplicado;
# · o valor do aumento;
# · o novo salário, após o aumento.
def main():
    salario = float(input('Digite o salário: '))
    percentual_de_aumento = definir_percentual(salario)
    aumento = calcular_aumento(salario)
    novo_salario = salario + aumento

    print(f"""
 ---------------------------------
 Salário: R${salario:.2f}
 Percentual de aumento: {percentual_de_aumento}
 Valor do aumento: R${aumento:.2f}
 Novo salário: R${novo_salario:.2f}
 ---------------------------------
 """)


def definir_percentual(salario):
    if salario <= 280:
        return '20%'
    elif salario <= 700:
        return '15%'
    elif salario <= 1500:
        return '10%'
    else:
        return '5%'

def calcular_aumento(salario: float):
    if salario <= 280:
        return (20 / 100) * salario
    elif salario <= 700:
        return (15 / 100) * salario
    elif salario <= 1500:
        return (10 / 100) * salario
    else:
        return (5 / 100) * salario





main()