import turtle

square = turtle.Turtle()

def criar_square(t,lenght: int):
    for i in range(4):
        t.fd(lenght)
        t.lt(90)

criar_square(square, 100)

turtle.done()