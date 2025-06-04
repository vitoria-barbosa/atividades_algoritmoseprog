# Escreva um algoritmo que calcula o retorno de um investimento financeiro. O usuário deve informar
# quanto será investido por mês e qual será a taxa de juros mensal. O algoritmo deve informar o saldo do
# investimento após um ano (soma das aplicações mensais + juros compostos), e perguntar ao usuário se
# deseja calcular o ano seguinte, sucessivamente. Por exemplo, caso o usuário deseje investir R$ 100,00
# por mês, e tenha uma taxa de juros de 1% ao mês, o algoritmo forneceria a seguinte saída:
# Saldo do investimento após 1 ano: 1268.25
# Deseja processar mais um ano (S/N) ?
from utils import obter_num_float
def main():
    capital_mes = obter_num_float("\nQuanto será investido por mês: ")
    taxa = obter_num_float("Valor da taxa de juros mensal(%): ")
    ano = 12
    
    saldo = calcular_juros_compostos(capital_mes, taxa, ano)

    print(f"\nSaldo do investimento após um ano: {saldo:.2f}")
    opcao = input("Deseja processar mais um ano (S/N)? ")

    while opcao != "n":
        ano += 12
        saldo = calcular_juros_compostos(capital_mes, taxa, ano)

        print(f"\nSaldo do investimento após um ano: {saldo:.2f}")

        opcao = input("Deseja processar mais um ano (S/N)? ")

    print("Fim.")
    

def calcular_juros_compostos(capital, taxa, tempo):
    i = taxa / 100
    return capital * (((1 + i)**tempo) - 1) / i

main()