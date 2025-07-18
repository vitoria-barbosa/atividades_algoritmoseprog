import utils as u

def carregar_dados():
    escolas = []
    arquivo = open("enem2014_nota_por_escola.txt")

    for linha in arquivo:
        dados = linha.strip().split(';')
        escola = {'ranking': dados[0], 'nome': dados[1], 'municipio': dados[2], 'uf': dados[3], 'rede': dados[4], 'permanencia': dados[5], 'nivel_socio_economico': dados[6], 'media_objetivas': dados[7].replace(',', '.'), 'linguagens': dados[8].replace(',', '.'), 'matematica': dados[9].replace(',', '.'), 'natureza': dados[10].replace(',', '.'), 'humanas': dados[11].replace(',', '.'), 'redacao': dados[12].replace(',', '.')}
        escolas.append(escola)
    
    return escolas


def mostrar_n_top_escolas(lista):
    n = u.obter_num_int("\nQuantidade de escolas que quer ver: ")

    print(f"\n>>> Melhores {n} Escolas do Brasil no ENEM 2014 <<<\n")

    for i in range(n):
        escola = lista[i]
        nome = f'N°{escola['ranking']} - {escola['nome']} - Média prova objetiva: {escola['media_objetivas']}'
        print(nome)

    return


def mostrar_n_top_escolas_area(lista):
    n = u.obter_num_int("\nQuantidade de escolas que quer ver: ")
    area = input("Área do conhecimento (linguagens/matematica/natureza/humanas/redacao): ")

    lista_ordenada = sorted(lista, key=lambda x: x[area], reverse=True)
    
    print(f"\n>>> Melhores {n} Escolas do Brasil em {area} no ENEM 2014 <<<\n")

    for i in range(n):
        escola = lista_ordenada[i]
        nome = f'N°{i+1} - {escola['nome']} - Média {area}: {escola[area]}'
        print(nome)

    return


def mostrar_melhor_escola_por_area(lista):
    area = input("Área do conhecimento (linguagens/matematica/natureza/humanas/redacao): ")
    lista_ordenada = sorted(lista, key=lambda x: x[area], reverse=True)

    print(f"\n>>> Escola com melhor desempenho em {area} do Brasil <<<\n")

    for i in range(1):
        escola = lista_ordenada[i]
        nome = f'N°{i+1} - {escola['nome']} - Média {area}: {escola[area]}'
        print(nome)

    return

def mostrar_n_top_escolas_estado(lista):
    n = u.obter_num_int("\nQuantidade de escolas que quer ver: ")
    estado = input("Estado (ex:PI): ").upper()
    
    lista_filtrada = filtrar(lista, lambda x: x['uf'] == estado)

    print(f"\n>>> Melhores {n} Escolas do/de {estado} no ENEM 2014 <<<\n")

    for i in range(n):
        escola = lista_filtrada[i]
        nome = f'N°{i+1} - {escola['nome']} - Média Geral: {escola['media_objetivas']}'
        print(nome)

    return


def mostrar_ranking_por_estado(lista):
    estado = input("\nEstado (ex:PI): ").upper()
    lista_filtrada = filtrar(lista, lambda x: x['uf'] == estado)

    print(f"\n>>>>>> Melhores Escolas do/de {estado} no ENEM 2014 <<<<<<\n")

    for i in range(len(lista_filtrada)):
        escola = lista_filtrada[i]
        nome = f'N°{i+1} - {escola['nome']} - Média Geral: {escola['media_objetivas']}'
        print(nome)

    return


def mostrar_melhor_escola_area_estado(lista):
    estado = input("\nEstado (ex:PI): ").upper()
    area = input("Área do conhecimento (linguagens/matematica/natureza/humanas/redacao): ")
    
    lista_filtrada = filtrar(lista, lambda x: x['uf'] == estado)
    lista_ordenada = sorted(lista_filtrada, key=lambda x: x[area], reverse=True)
    
    print(f"\n>>>> Melhor escola do/de {estado} em {area} <<<<\n")

    for i in range(1):
        escola = lista_ordenada[i]
        nome = f'N°{i+1} - {escola['nome']} - Estado: {estado} - Média {area}: {escola[area]}'
        print(nome)

    return


def mostrar_melhor_escola_area_todos_estados(lista):
    area = input("\nÁrea do conhecimento (linguagens/matematica/natureza/humanas/redacao): ")
    
    melhores = {}  # Aqui vamos guardar a melhor escola de cada estado

    for escola in lista:  # Percorre cada escola na lista
        estado = escola["uf"]  # Pega o estado da escola
        nota = float(escola.get(area, 0))  # Pega a nota da escola na área escolhida

        # Se ainda não temos escola para esse estado
        # ou se a escola atual tem nota maior que a armazenada
        if estado not in melhores or float(melhores[estado].get(area, 0)) < nota:
            melhores[estado] = escola  # Atualiza com a escola atual (que tem nota maior)
    
    print(f"\n>>>> Escolas com maior desempenho em {area} de cada estado do Brasil <<<<\n")
    
    for i in melhores:
        escola = melhores[i]
        nome = f'Estado: {escola['uf']} - {escola['nome']} -  Média {area}: {escola[area]}'
        print(nome)

    return


def mostrar_n_top_escolas_estado_rede(lista):
    n = u.obter_num_int("\nQuantidade de escolas que quer ver: ")
    estado = input("Estado (ex:PI): ").upper()
    rede = input("Rede (privada,federal,estadual,municipal): ")

    lista_filtrada1 = filtrar(lista, lambda x: x['uf'] == estado)
    lista_filtrada2 = filtrar(lista_filtrada1, lambda x: x['rede'].lower() == rede)

    if len(lista_filtrada2) < n:
        print(f"\nNão há {n} escolas que satisfaçam os critérios. Tente novamente:")
        return mostrar_n_top_escolas_estado_rede(lista)

    print(f"\n>>> Melhores {n} Escola(s) {rede}(s)/(is) do/de {estado} no ENEM 2014 <<<\n")

    for i in range(n):
        escola = lista_filtrada2[i]
        nome = f'N°{i+1} - {escola['nome']} - Média Geral: {escola['media_objetivas']}'
        print(nome)

    return


def mostrar_ranking_por_regiao(lista):
    regiao = input("\nRegião (Norte/Nordeste/Centro-Oeste/Sudeste/Sul): ")

    regioes = {
    "norte": ["AC", "AP", "AM", "PA", "RO", "RR", "TO"],
    "nordeste": ["AL", "BA", "CE", "MA", "PB", "PE", "PI", "RN", "SE"],
    "centro-oeste": ["GO", "MT", "MS", "DF"],
    "sudeste": ["ES", "MG", "RJ", "SP"],
    "sul": ["PR", "RS", "SC"]
    }

    estados = regioes[regiao.lower()]
    lista_filtrada = filtrar(lista, lambda x: x['uf'] in estados)

    print(f"\n>>>>>> Melhores Escolas da região {regiao} no ENEM 2014 <<<<<<\n")

    for i in range(len(lista_filtrada)):
        escola = lista_filtrada[i]
        nome = f'N°{i+1} - {escola['nome']} - Estado: {escola['uf']} - Média Geral: {escola['media_objetivas']}'
        print(nome)

    return


def mostrar_escolas_ordenadas_renda(lista):
    estado = input("\nEstado (ex:PI): ").upper()
    ordem_nivel = {
        'muito alto': 0,
        'alto': 1,
        'medio alto': 2,
        'medio': 3,
        'medio baixo': 4,
        'baixo': 5,
        'muito baixo': 6
    }

    escolas_estado = filtrar(lista, lambda escola: escola['uf'] == estado)
    escolas_validas = filtrar(escolas_estado, lambda escola: escola['nivel_socio_economico'] != 'Sem informacao')
    escolas_ordenadas = sorted(escolas_validas, key=lambda x: ordem_nivel.get(x['nivel_socio_economico'].lower()))

    print(f">>>> Lista das escolas do/de {estado} ordenadas por renda<<<<\n")

    for i in range(len(escolas_ordenadas)):
        escola = escolas_ordenadas[i]
        nome = f'Estado: {escola['uf']} - {escola['nome']} -  Nível socio-econômico: {escola['nivel_socio_economico']}'
        print(nome)

    return


def buscar_escola_por_parte_nome(lista):
    parte = input("\nParte do nome da escola que quer buscar: \n").upper()

    for escola in lista:
        nome = escola['nome']
        if parte in nome:
            print(nome)

    return 


def mostrar_media_por_area(lista):
    area = input("Área do conhecimento (linguagens/matematica/natureza/humanas/redacao): ")
    somatorio = 0

    for item in lista:
        somatorio += float(item[area])

    media = somatorio / len(lista)
    print(f"\nMédia nacional de {area}: {media:.2f}")

    return


def filtrar(colecao, funcao_criterio):
    nova_colecao = []
    
    for item in colecao:
        if funcao_criterio(item):
            nova_colecao.append(item)

    return nova_colecao