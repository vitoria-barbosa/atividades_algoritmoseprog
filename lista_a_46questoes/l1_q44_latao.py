# 44. Sabendo que latão é constituído de 70% de cobre e 30% de zinco, escreva um algoritmo que calcule a quantidade de cada um desses componentes para se obter certa quantidade de latão (em kg), informada pelo usuário.

def principal():
    qntd_latao = float(input('Quantidade de latão (KG): '))
    qnt_cobre = calcular_porcentagem(qntd_latao,70)
    qnt_zinco = calcular_porcentagem(qntd_latao,30)

    print(f'Para fazer {qntd_latao} Kg de latão você precisará de {qnt_cobre:.2f} kg de cobre (70%) e {qnt_zinco:.2f} Kg de zinco (30%).')


def calcular_porcentagem(quantidade,porcentagem):
    return (porcentagem / 100) * quantidade

principal()
