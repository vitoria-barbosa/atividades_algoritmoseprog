def principal():
    # CDB - empréstimo do cliente ao banco
    capital = float(input('Valor a ser investido:'))
    taxa = int(input('Taxa de juros compostos a ser aplicada (de 0% a 20% ao ano):'))
    tempo = float(input('Tempo de validade do investimento em anos:'))
    montante = juros_compostos(capital,taxa,tempo)
    juros_cdb = calcular_juros(montante,capital)
    total_investimento = f"""
    ---------- CDB ----------
    Valor investido = R${capital:.2f}
    R${capital:.2f} rendendo durante {tempo} anos com taxa de {taxa}% gera R${juros_cdb:.2f} de juros compostos
    Valor total a receber (investidor): R${montante:.2f}
    """

    print(total_investimento)

    # CDC - empréstimo do banco para o cliente
    emprestimo = float(input('Valor do empréstimo:'))
    taxa_cdc = int(input('Taxa de juros compostos a ser aplicada (de 0% a 17% ao mês):'))
    quantidade_parcelas = int(input('Quantidade de parcelas (24x,36x ou 60x):'))
    montante_cdc = juros_compostos(emprestimo,taxa_cdc,quantidade_parcelas)
    juros_cdc = calcular_juros(montante_cdc,emprestimo)

    total_a_pagar = f"""
    ---------- CDC ----------
    Valor emprestado = R${emprestimo:.2f}
    R${emprestimo:.2f} com taxa de {taxa_cdc}% gera R${juros_cdc:.2f} de juros compostos
    Valor total a pagar: R${montante_cdc:.2f}
    Parcelamento: {quantidade_parcelas}x de R${montante_cdc / quantidade_parcelas:.2f}
    """

    print(total_a_pagar)

    lucro_banco = f"""


    ------------------------------------------------------------
                       >>>RECIBO BANCO<<<

    >>> CDB
    Capital investido: R${capital:.2f}
    Taxa:{taxa}%
    Juros:R${juros_cdb:.2f}
    >>> CDC
    Valor empréstimo:R${emprestimo:.2f}
    Taxa:{taxa_cdc}%
    Juros:R${juros_cdc:.2f}

    Lucro = Juros CDC - Juros CDB
    Valor lucrado = R${calcular_lucro_banco(juros_cdc,juros_cdb):.2f}
    """

    print(lucro_banco)


def calcular_juros(montante,capital):
   return montante - capital


def juros_compostos(capital,taxa,tempo):
    return capital * (((taxa / 100) + 1) ** tempo)


def calcular_lucro_banco(juros_cdc,juros_cdb):
    return juros_cdc - juros_cdb

principal()
