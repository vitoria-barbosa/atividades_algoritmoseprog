# Faça um programa para auxílio o Prof. Joaquim ter dados sobre rendimento numa avaliação que aplicou a seus aluno. O professor irá digitar as notas de seus alunos e você deve computar: Maior Nota Geral, Menor Nota Geral, Média Geral da turma,. Performance das Notas dos Homens(escala 0 a 100%), Performance das Mulheres (escala 0 a 100%). A entrada será Sexo (M ou F) e Nota (número entre 1 e 10). Encerra quando sexo for diferente de M e F. Mostre quanto alunos, quantos de cada sexo, também. Classifique o desempenho da turma, e também homens e mulheres, em:
#a. Péssimo [0 a 2]
#b. Ruim ]2 a 4]
#c. Regular [4 a 7[
#d. Bom [7 a 8[
#e. Excelente [8 a 10]
import os

def main():
    qtd_masc = 0
    qtd_fem = 0
    alunos = 0
    maior_nota = 0
    menor_nota = float('inf')
    soma_notas = 0
    soma_notas_masc = 0
    soma_notas_fem = 0

    while True:
        sexo = int(input('\nSexo do aluno(0 - Masculino | 1 - Feminino): '))
        if sexo != 1 and sexo != 0:
            break
        nota = float(input('Nota: '))
        if sexo == 0:
            qtd_masc += 1
            soma_notas_masc += nota
        elif sexo == 1:
            qtd_fem += 1
            soma_notas_fem += nota
        if nota > maior_nota:
            maior_nota = nota
        elif nota < menor_nota:
            menor_nota = nota
        alunos += 1
        soma_notas += nota
        limpar_tela()

    media_turma = soma_notas / alunos
    media_masc = soma_notas_masc / qtd_masc
    media_fem = soma_notas_fem / qtd_fem
    performance_masc = (soma_notas_masc / soma_notas) * 100
    performance_fem = (soma_notas_fem / soma_notas) * 100
    print(f"""
    ========== RESULTADO ==========
    >Total de alunos: {alunos}
    >Total de Homens: {qtd_masc}
    >Total de Mulheres: {qtd_fem}
    >Maior Nota Geral: {maior_nota}
    >Menor Nota Geral: {menor_nota}
    >Média Geral da turma: {media_turma:.1f}
    >Performance dos Homens: {performance_masc:.2f}%
    >Performance das Mulheres: {performance_fem:.2f}%
    >Desempenho da turma: {classificar_desempenho(media_turma)}
    >Desempenho Homens: {classificar_desempenho(media_masc)}
    >Desempenho Mulheres: {classificar_desempenho(media_fem)}
    """)


def classificar_desempenho(media):
    if media > 8:
        return 'Excelente'
    elif media > 6:
        return 'Bom'
    elif media > 4:
        return 'Regular'
    elif media > 2:
        return 'Ruim'
    else:
        return 'Péssimo'
    

def limpar_tela():
    os.system('cls')

main()