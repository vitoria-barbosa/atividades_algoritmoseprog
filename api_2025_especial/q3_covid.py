# Durante a Pandemia da COVID, diariamente o
# noticiário informava à população dados importantes sobre a
# evolução e controle da doença. Neste cenário, usa-se atualmente
# o conceitos de “Em queda”, “Em Alta” e “Em Estabilidade”
# baseada nos números do dia. Variações menores que 15% nos
# números indicam "Em Estabilidade".
# Construa um programa que calcule e classifique a variação dos
# dados de acordo com o explicado. As entradas são vários
# números que representam a quantidade casos no dia. Os
# operadores podem, por erro, digitar valores inválidos com letras,
# números negativos, ou outros valores absurdos.
# Considerar apenas os inteiros não negativos. O programa deve
# parar quando for digitado exatamente “fim”. Após cada número
# mostrar o conceito do dia, ou “valor não computador” caso o valor
# seja inválido. E após o fim, mostrar total de casos, e média de
# casos por dia.
# feita sexta-feira
def main():
    print("======= PANDEMIA COVID-19 =======")
    print("\nVeja a situação do dia pelo número de casos.")
    print("Para encerrar e ver os resultados digite fim.\n")
    total_casos = 0
    qtd_dias = 0
    anterior = 1
    
    while True:
        entrada = input("Quantidade de casos de COVID do dia: ")
        if entrada == "fim":
            break
        try:
            qtd_casos = int(entrada)

            if qtd_casos <= 0:
                print("Valor não computado.")
                continue

            atual = qtd_casos
            situacao = calcular_situacao(anterior, atual)
            print(situacao)

            anterior = atual
            total_casos += qtd_casos
            qtd_dias += 1

        except ValueError:
            print("Valor não computado.")
            continue

    media = total_casos / qtd_dias
    print(f'''
        > Total de casos: {total_casos}
        > Média: {media:.0f}''')


def calcular_situacao(anterior: int, atual: int):
    variacao_percentual = ((atual - anterior) / anterior) * 100
    if variacao_percentual < -15:
        return "Em queda"
    elif variacao_percentual > 15:
        return "Em alta"
    else:
        return "Em estabilidade"

main()