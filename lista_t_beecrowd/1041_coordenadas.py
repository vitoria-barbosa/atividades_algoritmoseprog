# Leia 2 valores com uma casa decimal (x e y), que devem representar as coordenadas de um ponto em um plano. A seguir, determine qual o quadrante ao qual pertence o ponto, ou se está sobre um dos eixos cartesianos ou na origem (x = y = 0).
def main():
    entrada = input("")
    x = float(entrada.split()[0])
    y = float(entrada.split()[1])
    coordenada = determinar_quadrante(x, y)
    print(coordenada)

def determinar_quadrante(x, y):
    if x == 0 and y == 0:
        return "Origem"
    elif x == 0:
        return "Eixo Y"
    elif y == 0:
        return "Eixo X"
    elif x > 0 and y > 0:
        return "Q1"
    elif x < 0 and y > 0:
        return "Q2"
    elif x < 0 and y < 0:
        return "Q3"
    else:
        return "Q4"
    

main()