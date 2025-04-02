def principal():
    fatura = float(input('Valor da fatura: '))
    valor_pago = float(input('Valor pago (mínimo ou mais): '))
    meses = int(input('Quantos meses você ficou sem pagar: '))
    saldo_devedor = fatura - valor_pago
    juros_rotativo = calcular_juros(saldo_devedor,12,meses)
    multa_atraso = calcular_juros(saldo_devedor,2,meses)
    juros_mora = calcular_juros(saldo_devedor,1,meses)
    juros_total = juros_rotativo + multa_atraso + juros_mora
    fatura_final = saldo_devedor + juros_rotativo + multa_atraso + juros_mora

    print('----------------------------------------')
    print(f'A fatura de valor R${fatura:.2f} subtraindo o valor pago de R${valor_pago:.2f}')
    print(f'ficou R${saldo_devedor:.2f}, porém após {meses} meses sem pagar,')
    print(f'acumulou um juros total de R${juros_total:.2f}')
    print(f'totalizando um montante de R${fatura_final:.2f}!')
    print(f'Sua fatura aumentou {aumento_percentual(saldo_devedor,fatura_final):.0f}% em relação à fatura inicial.')

def calcular_juros(saldo_devedor,taxa,meses):
    return (saldo_devedor * (((taxa / 100) + 1) ** meses)) - saldo_devedor


def aumento_percentual(saldo_devedor,fatura_final):
    return ((fatura_final - saldo_devedor) / saldo_devedor) * 100

principal()
