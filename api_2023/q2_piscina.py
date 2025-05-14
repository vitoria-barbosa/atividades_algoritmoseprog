# a. Calcule a capacidade máxima da piscina pedindo ao usuário as
# dimensões de largura, comprimento e profundidade (em cm). 1 litro é
# igual a 1000 cm3
# . Uma piscina por exemplo de capacidade →
# L=100cm x C=100cm x P=100cm → 1000 litros, e deve ser cheia até
# 850 litros apenas.
# b. Informe até quantos litros é recomendado encher a piscina.
# c. Peça ao usuário para informar o valor a ser pago por cada 1000 litros
# na concessionária de água de sua cidade, e informe quanto ele
# gastará para encher sua piscina;
# d. Mensalmente é necessário repor 10% da água devido a banho e
# evaporação, informe ao usuário também o gasto mensal para manter
# a piscina no nível ideal.
def main():
    altura = int(input("Altura da piscina(cm): "))
    largura = int(input("Largura(cm): "))
    profundidade = int(input('Profundidade(cm): '))
    valor_agua = float(input('\nPreço de 1000 litros de água: '))
    capacidade_max_cm = altura * largura * profundidade
    capacidade_max_litros = capacidade_max_cm / 1000
    max_litros = capacidade_max_litros * 0.85
    qtd_litros = qtd_litros_arrendonado(max_litros)
    valor_pago = qtd_litros * valor_agua
    qtd_repor = qtd_litros_arrendonado(max_litros * 0.10)
    valor_mensal = qtd_repor * valor_agua

    print(f"""
 -------------------------------
 Sua piscina tem A={altura}cm L={largura}cm e P={profundidade}cm
 Capacidade máxima: {capacidade_max_litros} litros
 Quantidade recomendada para encher(85%): {max_litros} litros
 Preço de 1000 litros de água: R${valor_agua:.2f}
 Valor a pagar: R${valor_pago:.2f}

 *Mensalmente é necessário repor 10% da água devido a banho e
 evaporação, logo:
 Gasto mensal para manter o nível da piscina: R${valor_mensal}
 """)

def qtd_litros_arrendonado(litros):
    qtd_litros = (litros / 1000)
    if qtd_litros % 1 != 0: # se qtd de litros não for inteira
        arrendondado = (qtd_litros // 1) + 1
        return arrendondado
    else:
        return qtd_litros

main()