# Calcule a quantidade de combustível que pode ser colocada em uma aeronave e verifique se a aeronave
# pode levantar vôo ou não. Considere os seguintes critérios:
# · O peso de decolagem da aeronave é sempre igual a 500.000 kg;
# · O peso de decolagem é composto pela soma do peso do combustível, do peso da carga, do peso dos
# passageiros;
# · O peso do combustível é a quantidade do combustível (em litros) multiplicada pelo fator 1.5kg/l;
# · A quantidade mínima de combustível para que a aeronave decole é de 10000 l;
# · O peso da carga é o somatório do peso dos “containers” de cargas em quilogramas.
# · O peso dos passageiros é o somatório do peso de cada passageiro e de todos os volumes da sua
# bagagem; cada passageiro tem o peso estimado de 70kg e cada volume de bagagem tem o peso
# estimado de 10kg.
# O algoritmo deve ler o números de containers e a seguir ler o peso de cada container. A seguir devem
# ser lidos os dados dos passageiros (número do bilhete, quantidade de bagagens) até que o número do
# bilhete seja igual a 0. Devem ser mostrados, a quantidade de passageiros, a quantidade total de volume
# de bagagem, o peso dos passageiros, o peso da carga, a quantidade possível de combustível, e uma
# mensagem indicando a liberação da decolagem ou não.
from utils import obter_num_int, obter_num_float
def main():
    qtd_containers = obter_num_int("Quantidade de containers: ")

    peso_carga = 0
    qtd_passageiros = 0
    bagagens_total = 0

    for i in range(1, qtd_containers+1, 1):
        peso = obter_num_float(f"\nPeso do container {i}(kg): ")
        peso_carga += peso

    while True:
        print("\n**** REGISTRO DO PASSAGEIRO ****")
        num_bilhete = obter_num_int("Número do bilhete do passageiro: ")
        if num_bilhete == 0:
            print("\nPassageiros registrados com sucesso!")
            break
        qtd = obter_num_int("Quantas bagagens: ")
        bagagens_total += qtd
        qtd_passageiros += 1

    somatorio_peso = peso_carga + 15000 + (qtd_passageiros * 70) + (bagagens_total * 10)
    situacao = "LIBERADA" if somatorio_peso <= 500000 else "NEGADA, peso excedido"
    resultado = f"""
 ======== RESULTADO ========
 Quantidade de passageiros: {qtd_passageiros}
 Quantidade de bagagens: {bagagens_total}
 Peso dos passageiros: em média 70 kg
 Peso da carga: em média 10 kg
 Quantidade possível de combustível: 10.000 L
 Peso total: {somatorio_peso:.0f} kg

 DECOLAGEM: {situacao}
 """
    print(resultado)

main()