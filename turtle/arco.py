import turtle
import math

arco = turtle.Turtle()

def arc(bob, r, angle): 
    """desenha um arco com raio e angulo,usando a função polyline, se angulo=360, desenha um círculos completo"""
    arc_length = 2 * math.pi * r * angle / 360
    lados = int(arc_length / 3) + 1
    step_length = arc_length / lados
    step_angle = float(angle) / lados
    polyline(bob, lados, step_length, step_angle)


def polyline(bob, lados, length, angle):
    """Desenha n segmentos de reta com o comprimento dado e
    ângulo (em graus) entre eles. t é um turtle.
    """ # docstring
    for i in range(lados):
        bob.fd(length)
        bob.lt(angle)

arc(arco, 150, 360)