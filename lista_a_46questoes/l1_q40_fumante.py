# 40. Calcule a quantidade de dinheiro gasta por um fumante. Dados de entrada: o número de anos que ele fuma, o no de cigarros fumados por dia e o preço de uma carteira (1 carteira tem 20 cigarros).

import math

def principal():
    anos = float(input('A quantos anos você fuma: '))
    cigarros_dia = int(input('Quantos cigarros fuma por dia: '))
    valor_carteira = float(input('Valor da carteira de cigarro: '))
    dias_total = anos * 365
    total_cigarros = dias_total * cigarros_dia
    carteiras_compradas = total_cigarros / 20
    carteiras_arrendondado = math.ceil(carteiras_compradas)
    valor_gasto = carteiras_arrendondado * valor_carteira

    print(f'Ao fumar durante {anos} anos, fumando {cigarros_dia} cigarros por dia, você comprou {carteiras_arrendondado} carteiras de 20 cigarros, que custando R${valor_carteira:.2f}, fez você gastar aproximadamente R${valor_gasto:.2f} com esse vício.')

principal()    
