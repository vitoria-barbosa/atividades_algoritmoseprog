# Leia data atual (dia, mês e ano) e data de nascimento (dia, mês e ano) de uma pessoa, calcule e escreva sua idade exata (em anos).

def main():
    print('Digite a data de hoje: \n')
    data_atual_dia = obter_numero_inteiro('Dia: ')
    data_atual_mes = obter_numero_inteiro('Mês: ')
    data_atual_ano = obter_numero_inteiro('Ano: ')
    print('Digite sua data de nascimento: ')
    data_nascimento_dia = obter_numero_inteiro('Dia: ')
    data_nascimento_mes = obter_numero_inteiro('Mês: ')
    data_nascimento_ano = obter_numero_inteiro('Ano: ')

    dias_totais_ano_nasc = dias_ano_nascimento(data_nascimento_dia, data_nascimento_mes, data_nascimento_ano)
    dias_totais_ate_hoje = dias_ano_atual(data_atual_dia,data_atual_mes,data_atual_ano)
    idade_em_dias = dias_totais_ate_hoje - dias_totais_ano_nasc
    # Transformar em anos
    anos = idade_em_dias // 365
    meses = (idade_em_dias % 365) // 30
    dias = (idade_em_dias % 365) % 30

    print(f'Sua idade é de aproximadamente {anos} anos, {meses} mês(es) e {dias} dia(s).')


def dias_ano_nascimento(dia,mes,ano_nascimento):
    dias_vividos =  ((12 - mes) * 30) + (30 - dia)
    dias_ate_ano_nascimento = (ano_nascimento - 1) * 365
    total_nasc = (365 - dias_vividos) + dias_ate_ano_nascimento
    return total_nasc

def dias_ano_atual(dia,mes,ano_atual):
    dias_ate_hoje = ((mes - 1) * 30) + dia
    dias_ate_ano_atual = (ano_atual - 1) * 365
    total = dias_ate_ano_atual + dias_ate_hoje
    return total

def obter_numero_inteiro(label: str):
  return int(input(label))

main()