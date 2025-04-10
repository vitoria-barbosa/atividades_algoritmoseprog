def principal():
    distancia = int(input('Distância total da viagem: '))
    valor_gasolina = float(input('Valor gasolina: '))
    rendimento_gasolina = int(input('Rendimento da gasolina (Km/L): '))
    valor_alcool = float(input('Valor álcool: '))
    rendimento_alcool = int(input('Rendimento do álcool (Km/L): '))
    porcentagem_motor_eletrico = int(input('Quantos % da viagem conseguirá usar o motor elétrico (custo zero): '))
    distancia_motor_combustao = distancia - calcular_porcentagem(porcentagem_motor_eletrico,distancia)
    litros_gasolina = calcular_litros(distancia_motor_combustao,rendimento_gasolina)
    litros_alcool = calcular_litros(distancia_motor_combustao,rendimento_alcool)
    valor_a_gastar_gasolina = litros_gasolina * valor_gasolina
    valor_a_gastar_alcool = litros_alcool * valor_alcool
    tabela_comparativa = f"""
    -------->>> TABELA COMPARATIVA <<<--------
    Sua viagem será de {distancia} quilômetros
    {porcentagem_motor_eletrico}% dela, ou seja, {calcular_porcentagem(porcentagem_motor_eletrico,distancia):.1f} quilômetros
    você usará o motor elétrico (custo zero)
    mas {distancia_motor_combustao} KM da viagem você precisará usar o motor a combustão.

    Segue os valores comparativos para ajudá-lo a pagar menos em sua viagem:
    Se optar por gasolina, que custa R${valor_gasolina:.2f} e rende {rendimento_gasolina} Km/L,
    você precisará abastecer {litros_gasolina} litros de gasolina 
    para rodar {distancia_motor_combustao} km, totalizando R${valor_a_gastar_gasolina:.2f}.
    Já se optar por álcool, que custa R${valor_alcool:.2f} e rende {rendimento_alcool} Km/L, 
    você precisará abastecer {litros_alcool} litros de álcool 
    para rodar {distancia_motor_combustao} km, totalizando R${valor_a_gastar_alcool}.
    """

    print(tabela_comparativa)


def calcular_porcentagem(porcentagem_motor_eletrico,distancia):
    return (porcentagem_motor_eletrico / 100) * distancia


def calcular_litros(distancia_motor_combustao,rendimento):
    return distancia_motor_combustao / rendimento


principal()
