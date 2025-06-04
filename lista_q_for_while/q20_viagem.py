# Considere que um carro vai fazer uma viagem entre duas cidades e que a distância a ser percorrida é de
# 600 km. No início da viagem, o carro está com o tanque cheio (50 litros). Durante o percurso foi usado
# um aparelho para medir o desempenho do carro, que mostrava, quando acionado, duas informações:
# · Distância percorrida desde a última medição;
# · Quantidade de litros consumidos para percorrer a distância indicada.
# Escreva um algoritmo que leia estas informações e escreva:
# · se o carro chegou ao seu destino (distância percorrida maior ou igual a 600 km);
# · se o carro parou antes de chegar por falta de combustível (consumo igual a 50 litros);
# · o consumo em km/l do carro.
from utils import obter_num_int
def main():
    litros = 50
    distancia_total = 0
    soma_consumo = 0
    qtd = 0

    while True:
        distancia = obter_num_int("\nDistância percorrida desde a última medição: ")
        if distancia == 0:
            break
        litros = obter_num_int("Quantidade de litros consumidos para percorrer a distância indicada: ")
        soma_consumo += distancia / litros
        distancia_total += distancia
        litros -= litros
        qtd += 1

    chegou = "Sim" if distancia_total >= 600 else "Não"
    parou = "Não" if litros >= 0 else "Sim"
    media_consumo = soma_consumo / qtd

    resultado = f"""
 ------------------------------------------------------------
 O carro chegou ao seu destino? {chegou}
 O carro parou antes de chegar por falta de combustível? {parou}
 Consumo médio em km/L do carro: {media_consumo:.1f}
 """
    print(resultado)


main()