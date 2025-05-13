import sys
sys.path.append('C:\\Users\\vitor\\algoritmos_e_prog\\lista_f_condicionais')

from package.io_utils import obter_numero_float

def main():
    print('\n>>>> CALCULADORA DE DESCONTOS <<<<\n')
    valor_compra = obter_numero_float('Valor da Compra: ')
    vip = input('É cliente VIP?(s/n): ')
    aniversariante = input('Está fazendo aniversário hoje?(s/n): ')

    print('\n---------------------------')
    print(f'VALOR: R${valor_compra}')
    valor_com_desconto = ha_desconto(valor_compra)
    desconto_vip = eh_vip(vip, valor_com_desconto)
    desconto_aniversariante = eh_aniversariante(aniversariante, valor_com_desconto)
    
    if eh_vip(vip, valor_com_desconto) and eh_aniversariante(aniversariante, valor_com_desconto):
      vip_e_aniversariante = valor_com_desconto * 0.92  # 8% de desconto
      print('-5% de desconto, por ser VIP')
      print('-3% de desconto, por ser seu aniversário!')
      print(f'VALOR TOTAL: R${vip_e_aniversariante}')
    elif eh_vip(vip, valor_com_desconto):
      print('-5% de desconto, por ser VIP')
      print(f'VALOR TOTAL: R${desconto_vip:.2f}')
    elif eh_aniversariante(aniversariante, valor_com_desconto):
      print('-3% de desconto, por ser seu aniversário!')
      print(f'VALOR TOTAL: R${desconto_aniversariante:.2f}')
    else:
      print(f'VALOR TOTAL: R${valor_com_desconto:.2f}')

    print('---------------------------')

def ha_desconto(valor):
    if valor > 500:
        print(f'-15% de desconto, pelo valor da compra')
        return valor * 0.85
    elif valor >= 200:
        print(f'-10% de desconto, pelo valor da compra')
        return valor * 0.90
    elif valor >= 100:
        print(f'-5% de desconto, pelo valor da compra')
        return valor * 0.95
    else:
        return valor
    

def eh_vip(vip, desconto):
    if vip == 'sim':
        return desconto * 0.95
    elif vip == 'nao':
        return False
    else:
        print('Resposta inválida, digite sim ou nao. Tente novamente:')
        return eh_vip(desconto)
    

def eh_aniversariante(aniversariante, desconto):
    if aniversariante == 'sim':
        return desconto * 0.97
    elif aniversariante == 'nao':
        return False
    else:
        print('Resposta inválida, digite sim ou nao. Tente novamente:')
        return eh_aniversariante(desconto)

main()    