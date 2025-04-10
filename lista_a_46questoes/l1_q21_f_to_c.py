# Leia uma temperatura em °F, calcule e escreva a equivalente em °C.

def principal():
    fahrenheit = int(input('Temperatura em F°: '))

    print('----------- CONVERSOR DE TEMPERATURA -------------')
    print(f'>>>{fahrenheit} F° correspondem a {converter_temperatura(fahrenheit):.1f} C°.')

def converter_temperatura(temp):
    return (5 * temp - 160) / 9

principal()
