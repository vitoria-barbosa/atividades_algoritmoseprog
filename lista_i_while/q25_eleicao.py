# Em uma eleição presidencial existem 3 (três) candidatos. Os votos são informados através de códigos.Os dados utilizados para a contagem dos votos obedecem à seguinte codificação:
#· 1, 2, 3 = voto para os respectivos candidatos;
#· 9 = voto nulo;
#· 0 = voto em branco;
#Escreva um algoritmo que leia o código votado por N eleitores. Ao final, calcule e escreva:
#a) total de votos para cada candidato;
#b) total de votos nulos;
#c) total de votos em branco;
#d) quem venceu a eleição.
from package.io_utils import obter_numero_inteiro
import os

def main():
    qtd = obter_numero_inteiro('\nQuantidade de eleitores: ')
    limpar_tela()
    contador = 0
    voto_1 = 0
    voto_2 = 0
    voto_3 = 0
    voto_nulo = 0
    voto_branco = 0

    while contador < qtd:
        print(f"""
        ========= ELEIÇÃO =========
        Vote:
        1 - Lula
        2 - Bolsonaro
        3 - Simone Tebet
        9 - Nulo
        0 - Branco
        """)
        voto = obter_numero_inteiro('Digite o seu voto >>> ')
        if voto == 1:
            voto_1 += 1
        elif voto == 2:
            voto_2 +=1
        elif voto == 3:
            voto_3 += 1
        elif voto == 9:
            voto_nulo +=1
        else:
            voto_branco += 1
        contador += 1
        limpar_tela()
    
    vencedor = quem_venceu(voto_1, voto_2, voto_3)
    print(f"""
    Total de votos Lula: {voto_1}
    Total de votos Bolsonaro: {voto_2}
    Total de votos Simone Tebet: {voto_3}
    Total de votos nulos: {voto_nulo}
    Total de votos em branco: {voto_branco}
    VENCEDOR: {vencedor}
    """)


def quem_venceu(votos1, votos2, votos3):
    if votos1 > votos2 and votos1 > votos3:
        return 'LULA'
    elif votos2 > votos1 and votos2 > votos3:
        return 'BOLSONARO'
    elif votos3 > votos1 and votos3 > votos2:
        return 'SIMONE TEBET'
    else:
        return 'EMPATE'
    

def limpar_tela():
    os.system('cls')

main()