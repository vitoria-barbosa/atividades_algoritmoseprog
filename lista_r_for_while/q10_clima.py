# Contexto/Problema: Um pesquisador climático deseja analisar as tendências de temperatura máxima
# anual ao longo de uma série de anos. O programa deve permitir que o usuário insira o número de anos
# para os quais os dados serão registrados. Para cada ano, o usuário deve informar a temperatura
# máxima média anual. O programa deve identificar o ano com a maior temperatura, o ano com a menor

# temperatura, e calcular a média das temperaturas anuais. Além disso, deve indicar se houve uma
# tendência de aquecimento (se a média dos últimos anos for maior que a média dos primeiros anos).
# ● Entrada: O usuário deve informar a quantidade de anos para análise. Para cada ano, o usuário deve
# informar a temperatura máxima média anual.
from utils import obter_num_int, obter_num_float
def main():
    print("\n======= MONITORADOR DE TEMPERATURA ========")
    qtd_anos = obter_num_int("Quantidade de anos para análise: ")
    soma_metade1 = 0
    soma_metade2 = 0
    maior_temp = 0
    menor_temp = 10000
    metade = qtd_anos / 2
    soma_temperaturas = 0

    for i in range(1, qtd_anos+1, 1):
        print(f"\nAno {i}: ")
        temperatura = obter_num_float("Temperatura máxima média(°C): ")
        soma_temperaturas += temperatura

        if i <= metade:
            soma_metade1 += temperatura
        else:
            soma_metade2 += temperatura

        if temperatura > maior_temp:
            maior_temp = i
        if temperatura < menor_temp:
            menor_temp = i
    
    media_metade1 = soma_metade1 / metade
    media_metade2 = soma_metade2 / metade
    media_geral = soma_temperaturas / qtd_anos
    situacao = "Tendência de aquecimento" if media_metade2 > media_metade1 else "Tendência de resfriamento"

    resultado = f"""
 -----------------------------------
 Ano com maior temperatura: Ano {maior_temp}
 Ano com menor temperatura: Ano {menor_temp}
 Média geral da temperatura: {media_geral:.1f}°C
 Situação: {situacao}
 """
    print(resultado)


main()