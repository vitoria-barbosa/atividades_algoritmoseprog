import turtle

poligono = turtle.Turtle()

def polyline(t, length, lados):
    """Desenha n segmentos de reta com o comprimento dado e
    ângulo (em graus) entre eles. t é um turtle.
    """ # docstring
    angle = 360 / lados
    for i in range(lados):
        t.fd(length)
        t.lt(angle)

polyline(poligono, 100, 5)

turtle.done()