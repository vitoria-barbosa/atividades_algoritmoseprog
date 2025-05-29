# Uma determinada empresa armazena para cada funcionário uma ficha contendo o código, o número de horas trabalhadas e o seu num de dependentes. Considerando que a empresa paga R$ 12,00 por hora e R$ 40,00 por dependentes e que sobre o salário são feitos descontos de 8,5% para o INSS e 5% para IR. Escreva um algoritmo que leia o código, número de horas trabalhadas e número de dependentes de N funcionários. Após a leitura de cada ficha, escreva os valores descontados para cada imposto e o salário líquido do funcionário.
from utils import obter_numero_int_min
from utils import obter_num_inteiro
import os
def main():
    qnt = obter_numero_int_min('Quantidade de funcionários: ', 1)
    
    for i in range(0, qnt, 1):
        print('\n========== FICHA =========')
        codigo = obter_num_inteiro('Código do funcionário: ')
        num_horas_trabalhadas = obter_num_inteiro('Número de horas trabalhadas: ')
        num_dependentes = obter_num_inteiro('Número de dependentes: ')
        # Processamento
        salario = calcular_salario(num_horas_trabalhadas, num_dependentes)
        desconto_inss = calcular_desconto(salario, 8.5)
        desconto_ir = calcular_desconto(salario, 5)
        novo_salario = salario - desconto_inss - desconto_ir
        
        print(f'\nCódigo: {codigo}')
        print(f'Salário: R${salario:.2f}')
        print(f'Desconto INSS(8.5%): {desconto_inss:.2f}')
        print(f'Desconto IR(5%): {desconto_ir:.2f}')
        print(f'Salário líquido: R${novo_salario}') 
        
        input("\nPressione <Enter> para continuar...")
        limpar_tela()


def calcular_salario(horas: int, dependentes: int) -> float:
    salario = 12 * horas + 40 * dependentes
    return salario


def calcular_desconto(salario: float, porcentagem: float):
    desconto = (porcentagem / 100) * salario
    return desconto

    
def limpar_tela():
    os.system('cls')

main()