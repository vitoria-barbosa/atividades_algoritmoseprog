# Uma loja vende seus produtos no sistema entrada mais duas prestações, sendo a entrada maior ou igual a cada uma das duas prestações; estas devem ser iguais, inteiras e as maiores possíveis.

def principal():
    valor_produto = float(input('Valor do produto: '))
    parcelas = valor_produto // 3
    entrada = (valor_produto % 3) + parcelas

    print(f'O produto de R${valor_produto:.2f} terá a entrada de R${entrada:.2f} e 2 parcelas de R${parcelas:.2}')

principal()
