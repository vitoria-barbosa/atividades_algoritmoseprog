# Neste mês de Junho a bandeira estabelecida pelo governo federal foi a Vermelha Patamar 2, que significa que a cada 100 KWh de
# consumo será acrescido uma taxa extra de R$ 8,00.
# O Cálculo da energia elétrica para o consumidor final é feito baseado em KWh e em faixas.
# Valores hipotéticos:

# ● Consumo de até 30KWh isento de tarifa.
# ● Até 100 KWh será cobrado R$ 0,59 por cada um cada de todo os KWh consumidos;
# ● acima de 100KWh o valor de R$ 0,75 por cada um de todos os KWh consumidos.

# Sobre o valor tarifado/apurado são 25% de ICMS e 15% de PIS/CONFIS.
# A taxa de iluminação pública é cobrada apenas para os consumidores que passarem de 80 KWh por mês, e custa 6% do valor tarifado (antes do
# impostos).
# Considerando os dados acima construa um software que receba dois dados:
# Leitura Atual e Leitura Anterior do medidor de energia e faça todo o cálculo do "Talão de Energia" conforme detalhado acima.
# Como saída apresente os dados que compõem assim como o valor total a ser pago.
# Exemplo:
# Consumo 000 KWh
# Valor Faturado R$ 0,00
# Bandeira R$ 0,00 (x bandeiras)
# ICMS R$ 0,00
# PIS/CONFIS
# Taxa Iluminação R$ 0,00
def main():
    # entrada
    leitura_atual = obter_num_inteiro('Leitura atual(KWh): ')
    leitura_anterior = obter_num_inteiro('Leitura anterior(KWh): ')
    # processamento
    consumo = leitura_atual - leitura_anterior
    valor_bandeira = calcular_bandeira(consumo)
    qtd_bandeiras = consumo // 100 if consumo > 0 else 0
    valor_tarifado = calcular_tarifa(consumo)
    icms = 25 / 100 * valor_tarifado
    pis_confis = 15 / 100 * valor_tarifado
    taxa_iluminacao_publica = taxa_iluminacao(consumo, valor_tarifado)
    valor_total = valor_tarifado + valor_bandeira + icms + pis_confis + taxa_iluminacao_publica 
    # saída
    print(f"""
 ============ TALÃO DE ENERGIA ============
 > Consumo: {consumo} KWh
 > Valor Tarifado: R$ {valor_tarifado:.2f}
 > Bandeira: R$ {valor_bandeira:.2f} ({qtd_bandeiras} bandeira(s))
 > ICMS: R$ {icms:.2f}
 > PIS/CONFIS: R$ {pis_confis:.2f}
 > Taxa Iluminação: R$ {taxa_iluminacao_publica:.2f}

 > Valor total a pagar: R$ {valor_total:.2f}
 ------------------------------------------
 """)


def taxa_iluminacao(consumo, valor_tarifado):
    if consumo > 80:
        return 6 / 100 * valor_tarifado
    else:
        return 0


def calcular_tarifa(consumo):
    if consumo > 100:
        return 0.75 * consumo
    elif consumo > 30:
        return 0.59 * consumo
    else:
        return 0


def calcular_bandeira(consumo):
    if consumo >= 100:
        total_bandeira = consumo // 100 * 8
        return total_bandeira
    else:
        return 0


def obter_num_inteiro(label):
    entrada = input(label)
    try:
        num = int(entrada)
        return num
    except ValueError:
        print('Entrada inválida, escreva um valor numérico. Tente novamente: ')

main()