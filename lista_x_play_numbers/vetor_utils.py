from random import randint
from utils import obter_num_em_faixa, obter_num_positivo

def inicializar_vetor():
    inicio = """

 >>>>>>>>>>>> Play Numbers <<<<<<<<<<<<

 Escolha como você quer inicializar o vetor:
 1 - Preencher com dados automáticos
 2 - Preencher individualmente cada número
 3 - Carregar os números de um arquivo

 Sua opção >>> """
    
    opcao = obter_num_em_faixa(inicio, 1, 3)
    vetor = []

    if opcao == 1:
        tamanho = obter_num_positivo("Tamanho do vetor: ")
        min, max = map(int, input("Valor mínimo e máximo: ").split())
        for _ in range(tamanho):
            n = randint(min, max)
            vetor.append(n)

    elif opcao == 2:
        tamanho = obter_num_positivo("Tamanho do vetor: ")
        min, max = map(int, input("Valor mínimo e máximo: ").split())
        
        for i in range(1, tamanho + 1):
            n = obter_num_em_faixa(f"Valor {i}: ", min, max)
            vetor.append(n)

    elif opcao == 3:
        nome = input("Nome do arquivo: ")
        arquivo = open(nome)

        for linha in arquivo:
            numero = int(linha.strip())
            vetor.append(numero)


    return vetor


def filtrar(colecao, funcao_criterio):
    nova_colecao = []
    
    for item in colecao:
        if funcao_criterio(item):
            nova_colecao.append(item)

    return nova_colecao


def reduzir(colecao, funcao_redutora, inicial):
    acumulado = inicial

    for item in colecao:
        acumulado = funcao_redutora(acumulado, item)

    return acumulado


def somar(valor1, valor2):
    return valor1 + valor2


def calcular_somatorio(lista):
    somatorio = reduzir(lista, somar, 0)

    return somatorio


def calcular_media(lista):
    return calcular_somatorio(lista) / len(lista)


def maior(valor1, valor2):
    return valor1 if valor1 > valor2 else valor2


def menor(valor1, valor2):
    return valor1 if valor1 < valor2 else valor2


def mapear(colecao, funcao_transformdora):
    nova_colecao = []

    for item in colecao:
        item_transformado = funcao_transformdora(item)
        nova_colecao.append(item_transformado)

    return nova_colecao


def resetar_vetor(lista):
    num = int(input("\nNúmero que quer colocar em todas posições: "))

    for i in range(len(lista)):
        lista[i] = num

    return lista


def menor_valor_e_posicao(lista):
    menor_valor = reduzir(lista, menor, 1000000)
    menor_posicao = 0

    for i in range(len(lista)):
        if lista[i] == menor_valor:
            menor_posicao = i + 1

    print(f"O menor valor do vetor é {menor_valor} na posicao {menor_posicao}")


def maior_valor_e_posicao(lista):
    maior_valor = reduzir(lista, maior, -1000000)
    maior_posicao = 0

    for i in range(len(lista)):
        if lista[i] == maior_valor:
            maior_posicao = i + 1

    print(f"O maior valor do vetor é {maior_valor} na posicao {maior_posicao}")


def embaralhar(lista):
    nova_colecao = []
    qtd_indices = len(lista) - 1

    for i in range(0, len(lista)):
        item_removido = lista.pop(randint(0, qtd_indices))
        nova_colecao.append(item_removido)
        qtd_indices -= 1

    return nova_colecao


def substituir_valores_negativos(lista, min, max):
    for i in lista:
        if lista[i] < 0:
            novo_valor = randint(min, max)
            lista[i] = novo_valor

    return lista


def remover_por_posicao(colecao, posicao):
    nova_colecao = []

    for i in range(0, len(colecao)):
        if i != posicao - 1:
            nova_colecao.append(colecao[i])

    return nova_colecao


def editar_por_posicao(colecao, posicao, novo_valor):
    nova_colecao = []

    for i in range(0, len(colecao)):
        if i != posicao - 1:
            nova_colecao.append(colecao[i])
        else:
            nova_colecao.append(novo_valor)

    return nova_colecao


def salvar_em_arquivo(lista):
    nome_arquivo = input("Digite o nome do arquivo: ")

    arquivo = open(nome_arquivo, "w")
    linha = ''

    for item in lista:
        linha += f"{item}\n"

    arquivo.write(linha)