import turtle
import math

circle = turtle.Turtle()

def polyline(t, lados, length, angle):
    """Desenha n segmentos de reta com o comprimento dado e
    ângulo (em graus) entre eles. t é um turtle.
    """ # docstring
    for i in range(lados):
        t.fd(length)
        t.lt(angle)


def arc(t, r, angle): 
    """desenha um arco com raio e angulo,usando a função polyline, se angulo=360, desenha um círculos completo"""
    arc_length = 2 * math.pi * r * angle / 360
    lados = int(arc_length / 3) + 1
    step_length = arc_length / lados
    step_angle = float(angle) / lados
    polyline(t, lados, step_length, step_angle)


def criar_circle(t,raio):
    arc(t, raio, 360) # refatoração

criar_circle(circle, 100)

turtle.done()