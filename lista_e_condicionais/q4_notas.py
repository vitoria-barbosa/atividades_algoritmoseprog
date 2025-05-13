# Desenvolva um programa que receba três notas de um aluno, calcule a média e determine sua situação com base nos critérios:
import sys
sys.path.append('C:\\Users\\vitor\\algoritmos_e_prog\\lista_f_condicionais')

from package.io_utils import obter_numero_float

def main():
    nota1 = obter_numero_float('Nota 1: ')
    nota2 = obter_numero_float('Nota 2: ')
    nota3 = obter_numero_float('Nota 3: ')

    media = calcular_media(nota1, nota2, nota3)
    situacao = situacao_media(media)
    print(f'\nSua média ficou {media:.1f} e sua situação é: {situacao}')


def calcular_media(n1,n2,n3):
    return (n1 + n2 + n3) / 3


def situacao_media(media):
    if media < 5:
        return 'Reprovado'
    elif media <= 6.9:
        return 'Recuperação'
    else:
        return 'Aprovado'


main()    