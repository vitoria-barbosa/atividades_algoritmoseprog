# # Murilo acabou de iniciar seu curso de
# # graduação na faculdade de ADS e precisa de sua ajuda para
# # organizar dados estatísticos com os veteranos. Ela gostaria de
# # saber quantos alunos têm desejo aptidão em quatro áreas
# # “tradicionais” do desenvolvimento.
# São elas: Frontend, Mobile, Backend e Dados. Para obter estas
# informações, ela sabe exatamente quantos alunos vai questionar
# previamente, o tipo de habilidade/área e as quantidades detalhadas.
# Ele agrupou a pesquisa em blocos, por exemplo abaixo
# começo: 11:20 fim: 12:10
from q1_number_utils import obter_numero_int_positivo

def main():
    print("\n======== PESQUISA ADS ========")
    qtd = obter_numero_int_positivo("Quantidade de alunos entrevistados: ")
    contador = qtd
    print("Principais áreas da programação: Frontend, Mobile, Backend e Dados\n")
    frontend = 0
    mobile = 0
    backend = 0 
    dados = 0

    while contador > 0:
        entrada = input("Digite a quantidade de alunos e a inicial da área desejada: ")
        n = int(entrada.split()[0])
        area = entrada.split()[1]

        if area.upper() == "F":
            frontend += n

        elif area.upper() == "M":
            mobile += n

        elif area.upper() == "B":
            backend += n

        else:
            dados += n

        contador -= 1

    total_alunos = frontend + mobile + backend + dados
    percentual_backend = backend / total_alunos * 100
    percentual_frontend = frontend / total_alunos * 100
    percentual_mobile = mobile / total_alunos * 100
    percentual_dados = dados / total_alunos * 100

    resultado = f"""
 ------------------------------
 Total: {total_alunos} alunos
 Total de Backend: {backend}
 Total de Frontend: {frontend}
 Total de Mobile: {mobile}
 Total de Dados: {dados}
 Percentual de Backend: {percentual_backend}%
 Percentual de Frontend: {percentual_frontend}%
 Percentual de Mobile: {percentual_mobile}%
 Percentual de Dados: {percentual_dados}%
 -------------------------------
 """
    print(resultado)

main()