# Faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# a) "Telefonou para a vítima ?"
# b) "Esteve no local do crime ?"
# c) "Mora perto da vítima ?"
# d) "Devia para a vítima ?"
# e) "Já trabalhou com a vítima ?"
# O algoritmo deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa
# responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como
# "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
def main():
    telefonou = pedir_resposta('\nTelefonou para a vítima? ')
    esteve_local = pedir_resposta('Esteve no local do crime? ')
    mora_perto = pedir_resposta('Mora perto da vítima? ')
    devia = pedir_resposta('Devia para a vítima? ')
    trabalhou = pedir_resposta('Já trabalhou com a vítima? ')
    qtd_sim = telefonou + esteve_local + mora_perto + devia + trabalhou
    situacao = classificar_situacao(qtd_sim)
    print(f'\nDe acordo com suas respostas, você é {situacao}')


def classificar_situacao(qtd_sim):
    if qtd_sim == 5:
        return 'ASSASSINO'
    elif qtd_sim > 2:
        return 'CÚMPLICE'
    elif qtd_sim == 2:
        return 'SUSPEITO'
    else:
        return 'INOCENTE'
    
        
def pedir_resposta(pergunta):
    resposta = validar_resposta(pergunta)
    if resposta == 'sim':
        return 1
    else:
        return 0
    

def validar_resposta(pergunta):
    entrada = input(pergunta)
    if entrada == 'sim' or entrada == 'nao':
        return entrada
    else:
        print('Essa resposta não é valida! Tente novamente: ')
        return validar_resposta(pergunta)
    
main()