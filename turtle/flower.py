import turtle

flor = turtle.Turtle()

def main():
    print(flor)
    criar_flor(9)


def criar_flor(num_petalas: int):
    angle = 360 / num_petalas
    for i in range(num_petalas):
        desenhar_petala(flor, 300, 55)
        flor.left(angle)


def desenhar_petala(t, raio, angulo):
    for _ in range(2):  # Dois arcos
        t.circle(raio, angulo)
        t.left(180 - angulo)


main()

turtle.done()
