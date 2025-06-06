from utils import obter_num_int, obter_num_float
def main():
    print("\n===== MONITORAMENTO CLIMÁTICO =====")
    qtd = obter_num_int("Quantidade de temperaturas: ")
    limite = obter_num_float("Limite de temperatura(°C): ")

    maior_temp = 0
    menor_umidade = 10000
    vezes_excedeu = 0

    for i in range(1, qtd+1, 1):
        print(f"\n- Temperatura {i}")
        temperatura = obter_num_float("- Temperatura(°C): ")
        umidade = obter_num_int("- Umidade(%): ")

        if temperatura > maior_temp:
            maior_temp = temperatura

        if umidade < menor_umidade:
            menor_umidade = umidade

        if temperatura > limite:
            vezes_excedeu += 1
        
    resultado = f"""
 -----------------------------------------------------
 > Maior temperatura registrada: {maior_temp}°C
 > Menor umidade registrada: {menor_umidade}%
 > Quantidade de vezes que ultrapassou {limite:.0f}°C: {vezes_excedeu} vezes
 """
    print(resultado)

main()