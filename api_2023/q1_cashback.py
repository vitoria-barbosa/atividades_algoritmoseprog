# Uma loja presenteia suas clientes com descontos
# (cashback) progressivos de acordo com suas compras. Desta
# forma, para compras mensais de até R$ 250 reais, é feita a
# conversão (geração) de cashback de 5%; Para compras acima de
# R$ 250 até R$ 500, 7% de cashback; De R$ 500 até R$ 750, 8%
# de cashback; E para compras acima de R$ 750 é aplicado
# primeiramente as regras anteriores até R$ 750 do valor em cada
# faixa, e 25% sobre o valor acima de R$ 750.
# a. Implemente um software para auxiliar no cálculo do
# cashback mensal de suas clientes (devem ser lidos N
# compras Nome Cliente e Valor Compras).
# b. Informe quanto foi o faturamento total (soma das vendas);
# Quanto foi distribuído em cashback; Qual o valor em reais e
# percentual investido em cashback pela loja; Maior, menor e
# valor médio pago em cashback.
def main():
    qtd_clientes = int(input('Quantidade de clientes: '))
    contador = qtd_clientes
    soma_vendas = 0
    maior_cashback = 0
    menor_cashback = 10000
    total_cashback = 0

    while contador > 0:
        input('Nome da cliente: ')
        valor_compra = float(input('Valor da compra(R$): '))
        cashback = calcular_cashback(valor_compra)
        if cashback > maior_cashback:
            maior_cashback = cashback
        if cashback < menor_cashback:
            menor_cashback = cashback
        total_cashback += cashback
        soma_vendas += valor_compra
        contador -= 1

    percentual_cashback = (total_cashback / soma_vendas) * 100
    valor_medio_cashback = total_cashback / qtd_clientes

    print(f"""
 ========= FECHAMENTO DO MÊS ===========
 Faturamento total: R${soma_vendas:.2f}
 Valor total investido em cashback: R${total_cashback:.2f}
 Percentual investido em cashback: {percentual_cashback:.1f}%
 Maior Cashback: R${maior_cashback:.2f}
 Menor Cashback: R${menor_cashback:.2f}
 Valor médio em cashback: {valor_medio_cashback:.2f}
 """)
    

def calcular_cashback(valor):
    if valor <= 250:
        cashback = (5/100) * valor
        return cashback
    elif valor < 500:
        cashback = (7/100) * valor
        return cashback
    elif valor < 750:
        cashback = (8/100) * valor
        return cashback
    else:
        restante = valor - 750
        cashback = (5/100) * 250 + (7/100) * 250 + (8/100) * 250 + (25/100) * restante
        return cashback
    
main()