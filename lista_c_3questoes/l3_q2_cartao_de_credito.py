def principal():
    # input
    print('\nOpção 1 de pagamento:')

    faturap1 = float(input('Valor da fatura: '))
    valor_pagop1 = float(input('Valor pago (mínimo ou mais): '))
    mesesp1 = int(input('Quantos meses você ficou sem pagar: '))

    print('\nOpção 2 de pagamento:')

    faturap2 = float(input('Valor da fatura: '))
    valor_pagop2 = float(input('Valor pago (mínimo ou mais): '))
    mesesp2 = int(input('Quantos meses você ficou sem pagar: '))

    # pagamento 1
    saldo_devedorp1 = faturap1 - valor_pagop1
    juros_totalp1 = calcular_juros(saldo_devedorp1,15,mesesp1)
    fatura_finalp1 = saldo_devedorp1 + juros_totalp1
    # pagamento 2
    saldo_devedorp2 = faturap2 - valor_pagop2
    juros_totalp2 = calcular_juros(saldo_devedorp2,15,mesesp2)
    fatura_finalp2 = saldo_devedorp2 + juros_totalp2

    # output
    # pagamento 1
    print('\n------------------- OPÇÃO DE PAGAMENTO 1 -----------------------')
    print(f'\nA fatura de valor R${faturap1:.2f} subtraindo o valor pago de R${valor_pagop1:.2f}')
    print(f'fica R${saldo_devedorp1:.2f}, porém após {mesesp1} meses sem pagar,')
    print(f'acumula um juros total de R${juros_totalp1:.2f}')
    print(f'totalizando um montante de R${fatura_finalp1:.2f}!')
    print(f'Sua fatura aumentou {aumento_percentual(saldo_devedorp1,fatura_finalp1):.0f}% em relação à fatura inicial.')
    # pagamento 2
    print('\n------------------ OPÇÃO DE PAGAMENTO 2 ------------------------')
    print(f'\nA fatura de valor R${faturap2:.2f} subtraindo o valor pago de R${valor_pagop2:.2f}')
    print(f'fica R${saldo_devedorp2:.2f}, porém após {mesesp2} meses sem pagar,')
    print(f'acumula um juros total de R${juros_totalp2:.2f}')
    print(f'totalizando um montante de R${fatura_finalp2:.2f}!')
    print(f'Sua fatura aumentou {aumento_percentual(saldo_devedorp2,fatura_finalp2):.0f}% em relação à fatura inicial.')

def calcular_juros(saldo_devedor,taxa,meses):
    return (saldo_devedor * (((taxa / 100) + 1) ** meses)) - saldo_devedor


def aumento_percentual(saldo_devedor,fatura_final):
    return ((fatura_final - saldo_devedor) / saldo_devedor) * 100

principal()
