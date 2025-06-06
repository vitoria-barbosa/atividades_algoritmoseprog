# Saída Esperada: A média calórica diária do período, o dia com o menor consumo, o dia com o maior
# consumo, e uma mensagem indicando se a média diária de calorias excedeu ou não o limite informado.
from utils import obter_num_int
def main():
    dias = obter_num_int("\nDurante quantos dias você quer analisar suas calorias: ")
    limite_calorias = obter_num_int("Limite de calorias: ")
    somatorio_medias = 0
    maior_consumo = 0
    dia_maior_consumo = 0
    menor_consumo = 100000
    dia_menor_consumo = 0

    for i in range(1, dias+1, 1):
    
        print(f"\nDia {i}: ")
        cafe = obter_num_int("Calorias consumidas no café da manhã: ")
        almoco = obter_num_int("Calorias consumidas no almoço: ")
        lanche = obter_num_int("Calorias consumidas no lanche: ")
        janta = obter_num_int("Calorias consumidas no jantar: ")

        consumo_dia = cafe + almoco + lanche + janta
        if consumo_dia > maior_consumo:
            maior_consumo = consumo_dia
            dia_maior_consumo = i
        if consumo_dia < menor_consumo:
            menor_consumo = consumo_dia
            dia_menor_consumo = i

        media_diaria = consumo_dia / 4
        somatorio_medias += media_diaria
        media_semanal = somatorio_medias / dias
        situacao = "Dentro do limite" if media_semanal <= limite_calorias else "Limite ultrapassado"

    resultado = f"""
 ====== Análise de Consumo de Calorias ======
 Média calórica diária dos {dias} dias: {media_semanal:.1f} calorias
 Dia com o menor consumo: Dia {dia_menor_consumo} com {menor_consumo} calorias
 Dia com maior consumo: Dia {dia_maior_consumo} com {maior_consumo} calorias
 Limite: {limite_calorias} calorias
 Situação: {situacao}
 """
    print(resultado)

main()