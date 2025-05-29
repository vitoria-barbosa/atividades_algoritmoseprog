# A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o salário e número de filhos. Escreva um algoritmo que leia o salário e o número de filhos de N habitantes e escreva:
# a) média de salário da população;
# b) média de número de filhos;
# c) percentual de pessoas com salário de até R$ 1.000,00.
from utils import obter_num_inteiro
import os

def main():
    qtd = obter_num_inteiro('Quantidade de habitantes: ')
    limpar_tela()
    soma_salario = 0
    soma_filhos = 0
    qtd_menor_que_mil = 0

    for i in range(0, qtd, 1):
        salario = float(input('Salário: '))
        qtd_filhos = obter_num_inteiro('Número de filhos: ')
        if salario <= 1000:
            qtd_menor_que_mil += 1
        soma_salario += salario
        soma_filhos += qtd_filhos
        limpar_tela()

    media_salario = soma_salario / qtd
    media_filhos = soma_filhos / qtd
    porcentagem_ate_mil = (qtd_menor_que_mil / qtd) * 100

    resultado = f"""
    ====== RESULTADO ======
    Média de salário da população: R${media_salario:.2f}
    Média de número de filhos: {media_filhos:.1f}
    Percentual de pessoas com salário de até R$ 1.000,00: {porcentagem_ate_mil:.1f}%
    """
    print(resultado)


def limpar_tela():
    os.system('cls')

main()