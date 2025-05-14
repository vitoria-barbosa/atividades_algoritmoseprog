# Mariana resolveu investir de parte de seu salário
# (um pedaço(R$) inferior a 30%) de forma fixa mensal; O investimento
# escolhido rende mensalmente a uma taxa de juros de 0,01% até 1,00
# % sobre o saldo do mês. Mariana tem um dado objetivo com este
# investimento. Pergunte a ela qual o objetivo e de quanto ela precisa
# para realizá-lo. Além disso, peça o salário, quanto(%) ela pretende
# investir mensalmente e qual a taxa de juros do investimento
# escolhido. Em seguida mostre em quantos meses ela atingirá o
# objetivo. Se for acima de 12 meses mostre-o em anos e meses. A
# cada mês você deve atualizar o saldo primeiro com o aporte
# (depósito de valor do salário) e depois aplicar os créditos dos juros
# sobre esse novo saldo. Faça isso enquanto o objetivo não for
# alcançado, contando os meses para serem exibidos como se pede.
def main():
    # entrada
    input('Para qual objetivo você quer juntar seu dinheiro: ')
    meta_valor = obter_valor_na_faixa('De quanto você precisa para isso: ', 1, 100000)
    salario = obter_valor_na_faixa('Valor do seu salário: ', 1, 100000)
    percentual_do_salario = obter_valor_na_faixa('Quantos % do seu salário pretende investir: ', 1, 30)
    taxa_percentual = obter_valor_na_faixa('Taxa de juros ao mês(%): ', 0.01, 1)

    # processamento
    taxa = taxa_percentual / 100
    capital_investido = salario * (percentual_do_salario/100)
    saldo_investimento = capital_investido
    qtd_meses = 0

    while saldo_investimento < meta_valor: 
        juros = saldo_investimento * taxa
        saldo_investimento = saldo_investimento + juros + capital_investido
        qtd_meses += 1
        
    tempo = calcular_tempo(qtd_meses)
    print('----------------------------')
    print(f'Para juntar R${meta_valor:.2f}, demorará {tempo}')
    print(saldo_investimento)


def calcular_tempo(qtd_meses: int):
    if qtd_meses <= 12:
        return f'{qtd_meses} meses'
    else:
        anos = qtd_meses // 12
        meses = qtd_meses % 12
        return f'{anos} anos e {meses} mes(es)'


def obter_valor_na_faixa(label: str,min: int, max: int):
    entrada = (input(label))
    try:
        valor = float(entrada)
        if valor > max or valor < min:
            print(f'Valor fora da faixa, escreva um valor entre {min} e {max}. Tente novamente: ')
            return obter_valor_na_faixa(label, min, max)
        else:
            return valor
    except ValueError:
        print('Entrada inválida! Escreva valores numéricos. Tente novamente: ')
        return obter_valor_na_faixa(label, min, max)


main()