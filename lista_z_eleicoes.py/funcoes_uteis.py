def carregar_partidos():
    coligacoes = []
    arquivo = open("partidos_coligacoes_the_2012.csv")

    for linha in arquivo:
        nome = linha.strip()
        coligacao = {'coligacao': nome, 'total_votos': 0, 'qtd_vagas': 0}

        coligacoes.append(coligacao)

    return coligacoes


def carregar_candidatos():
    candidatos = []
    arquivo = open("candidatos_e_votos.csv")

    for linha in arquivo:
        dados = linha.strip().split(';')
        candidato = {'nome': dados[0], 'numero': dados[1], 'nome_partido': dados[2], 'coligacao': dados[3], 'total_votos': int(dados[4])}

        candidatos.append(candidato)

    candidatos = sorted(candidatos, key= lambda x: x['total_votos'], reverse=True)

    return candidatos


def computar_total_votos_por_coligacao(lista_coligacoes, lista_candidatos):
    
    for partido in lista_coligacoes:
        total = 0
        for candidato in lista_candidatos:
            if candidato['coligacao'] == partido.get('coligacao'):
                total += candidato['total_votos']
    
        partido['total_votos'] = total

    return lista_coligacoes


def calcular_quociente_partidario(coligacoes, quociente_eleitoral):

    for coligacao in coligacoes:
        if coligacao.get('total_votos') >= quociente_eleitoral:
            vagas = coligacao.get('total_votos') // quociente_eleitoral

            coligacao['qtd_vagas'] = vagas

    return coligacoes


def distribuir_vagas_restantes(coligacoes, vagas_restantes):

    for _ in range(vagas_restantes):
        maior = 0
        for coligacao in coligacoes:
            media = coligacao['total_votos'] / (coligacao['qtd_vagas'] + 1)
            if media > maior:
                maior = media
                maior_coligacao = coligacao
            
        maior_coligacao['qtd_vagas'] += 1

    return coligacoes


def somar_votos(lista):
    somatorio = 0

    for candidato in lista:
        votos = candidato.get('total_votos')
        somatorio += votos

    return somatorio


def calcular_quociente_eleitoral(votos_total, qtd_vagas):
    return votos_total // qtd_vagas