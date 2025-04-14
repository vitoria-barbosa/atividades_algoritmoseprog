import turtle
import math

torta =  turtle.Turtle()

def main():
	print(torta)
	criar_torta(torta, 100, 5)
	

def criar_torta(t,length,n):	
	vertice = (length/2)/math.sin(math.radians(180/n))
	for i in range(n):
		t.fd(length)
		t.lt(90 + (180/n))
		t.fd(vertice)
		t.lt(180)
		t.pu()
		t.fd(vertice)
		t.lt(90 + (180/n))
		t.pd()		
		
main()

turtle.mainloop()