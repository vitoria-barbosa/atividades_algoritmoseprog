# José está planejando uma viagem com sua família para a Capital Federal. Para isso tem juntado Milhas em programas de fidelidade, e também pesquisando passagens aéreas diretamente. No Programa Smiles é possível comprar Milhas Aéreas pagando 70 reais a cada 1000 unidades. Uma passagem Teresina(THE) para Brasília(BSB) custa em torno de 21200 milhas, o mesmo voo(horário) tá por R$ 431. Ou seja, nesse caso, é melhor comprar em R$ que comprar Milhas a R$ 70/Milheiro para então emitir o Voo. Entretanto no mundo das milhas, nunca compramos milhas a esse valor de 70 reais por mil, o que se faz é acumular milhas por meio de Cartão de Crédito e Compras Bonificadas. Neste caso, precifica-se as Milhas (valor convencionado) como baratas a R$ 14,50 o Milheiro. Assim, o voo exemplificado acima as 21200 Milhas custariam em reais o total de R$ 307,40. Desta forma, sendo vantajoso, ou seja, custa apena 71,3% do valor em R$ normal (R$ 431) Faça um programa para auxiliar José no comparativo dos valor das passagens com Milhas Padrão(R$ 70), Milhas Acumuladas Baratas (R$ 14,50) e em Reais Normal (valor do site). Peça ao usuário Origem, Destino, Valor em R$ no site e Valor em Milhas no Site. Apresente para ele o valor equivalente em R$ caso compre com Milhas Padrão, indicando o % em relação ao valor em R$. Faça o mesmo para Milhas Baratas. Ao final, indique para ele a melhor forma de compra dentre as 3 opções.
from utils import obter_numero_float_positivo

def main():
    print('\n====== COMPRE SUA PASSAGEM =====')
    input('Origem: ')
    input('Destino: ')
    valor_reais = obter_numero_float_positivo('Valor da passagem(R$): ')
    valor_milhas = obter_numero_float_positivo('Valor da passagem(Milhas): ')
    # Processamento:
    qtd_milhas = valor_milhas / 1000
    valor_milhas_padrao = qtd_milhas * 70
    valor_milhas_baratas = qtd_milhas * 14.50
    porcentagem_milhas_padrao = (valor_milhas_padrao / valor_reais) * 100
    porcentagem_milhas_baratas = (valor_milhas_baratas / valor_reais) * 100
    mais_barato = qual_comprar(valor_reais, valor_milhas_padrao, valor_milhas_baratas)
    comparacao = f"""\n
    ====== COMPARATIVO =====
    > Valor em reais: R$ {valor_reais}
    > Milhas Padrão: R$ 70/milheiro
      Valor a pagar: R$ {valor_milhas_padrao:.2f}
      {porcentagem_milhas_padrao:.1f}% em relação ao valor em reais
    > Milhas Acumuladas Baratas: R$ 14,50/milheiro
      Valor a pagar: R$ {valor_milhas_baratas:.2f}
      {porcentagem_milhas_baratas:.1f}% em relação ao valor em reais
    
    VALE MAIS A PENA: {mais_barato}
    """
    print(comparacao)


def qual_comprar(valor_reais, valor_milhas_padrao, valor_milhas_baratas):
    if valor_reais < valor_milhas_padrao and valor_reais < valor_milhas_baratas:
        return 'Valor Normal em reais'
    if valor_milhas_padrao < valor_reais and valor_milhas_padrao < valor_milhas_baratas:
        return 'Milhas padrão'
    if valor_milhas_baratas < valor_reais and valor_milhas_baratas < valor_milhas_padrao:
        return 'Milhas acumuladas baratas' 

main()