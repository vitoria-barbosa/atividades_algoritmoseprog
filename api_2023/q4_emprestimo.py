# Porém a taxa de juros aplicada é calculada de acordo com o prazo
# de parcelamento (vide tabela) e à SELIC, atualmente em 13,75%
# (abril/2023). O usuário só pode parcelar o empréstimo em até 24x
# (min. 2 parcelas). Valor mínimo de empréstimo é de um salário
# mínimo. Valor máximo de parcela é 40% da Renda Mensal do
# Cliente.
# Antes de calcular os juros é necessário calcular o IOF (Imposto sobre
# Operações Financeiras) pago ao Governo Federal antes de aplicar
# os Juros. O IOF é calculado da seguinte forma: 0,38% sobre valor
# total (independente do prazo) + 0,0082% por cada dia do prazo do
# empréstimo. Considere todos os meses com 30 dias. Os juros são
# aplicados sobre o valor a ser recebido pelo Cliente + IOF
# Peça ao usuário Renda Mensal, Valor Empréstimo e Prazo
# desejados, valide os dados a serem recebidos.
# ● Calcule e escreva na tela:
# a. Valor Pedido
# b. Valor do IOF
# c. Valor dos Juros a pagar
# d. Valor Total a pagar (ex.: "R$ 5148,00")
# e. Valor da Parcela Mensal (ex.: "16x de R$ 321,75")
# f. Comprometimento da Renda Mensal (%)
# g. Se Empréstimo APROVADO ou NEGADO (se a
# renda mensal suporta a parcela)
def main():
    renda_mensal = obter_valor_em_faixa("Sua Renda Mensal(R$): ", 1, 100000)
    valor_emprestimo = obter_valor_em_faixa("Valor do empréstimo: ", 1518, 100000)
    prazo = obter_valor_em_faixa("Prazo em que deseja parcelar: ", 2, 24)
    taxa_percentual = classificar_taxa(prazo)
    iof = calcular_iof(valor_emprestimo, prazo)
    valor_total = calcular_juros_compostos(iof, valor_emprestimo, taxa_percentual, prazo)
    juros = valor_total - valor_emprestimo 
    valor_parcela = valor_total / prazo
    situacao = classificar_situacao(renda_mensal, valor_parcela)
    comprometimento = valor_parcela / renda_mensal * 100

    print(f"""
 --------------------------------------------------------
 Valor Pedido: R${valor_emprestimo:.2f}
 Valor do IOF: R${iof:.2f}
 Valor dos Juros a pagar: R${juros:.2f}
 Valor Total a pagar: R${valor_total:.2f}
 Valor da Parcela Mensal: {prazo:.0f}x de {valor_parcela:.2f}
 Comprometimento da Renda Mensal: {comprometimento:.1f}%
 
 Situação: {situacao}
 --------------------------------------------------------
 """)
    

def classificar_situacao(renda, parcela):
    valor_max = 40 / 100 * renda
    if parcela >  valor_max:
        return "NEGADO. Sua renda mensal não suporta a parcela"
    else:
        return "APROVADO. Parabéns!"
    

def calcular_juros_compostos(iof, valor_emprestimo, taxa, prazo):
    montante = (valor_emprestimo + iof) * (1 + (taxa / 100)) ** prazo
    return montante


def calcular_iof(valor_emprestimo, prazo):
    dias = prazo * 30
    return ((0.38 / 100) * valor_emprestimo) + ((0.0082 / 100) * dias)


def classificar_taxa(prazo):
    if prazo < 6:
        return 50 / 100 * 13.75
    elif prazo < 12:
        return 75 / 100 * 13.75
    elif prazo < 18:
        return 13.75
    else:
        return 130 / 100 * 13.75
    

def obter_valor_em_faixa(label: str, min: int, max: int):
    entrada = input(label)
    try:
        valor = float(entrada)
        if valor > max or valor < min:
            print(f"Escreva um valor entre {min} e {max}. Tente novamente: ")
            return obter_valor_em_faixa(label, min, max)
        else:
            return valor
    except ValueError:  
        print("Entrada inválida, escreva um valor numérico. Tente novamente: ") 
        return obter_valor_em_faixa(label, min, max)

main()