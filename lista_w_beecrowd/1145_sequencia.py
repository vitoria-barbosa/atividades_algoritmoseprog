# Escreva um programa que leia dois valores X e Y. A seguir, mostre uma sequência de 1 até Y, passando para a próxima linha a cada X números.
def main():
    x, y = map(int, input().split())

    contador = 1
    while contador <= y:
        
        for i in range(x):
            
            if i == x-1:
                print(contador)
            else:
                print(contador, end=" ")
                
            contador += 1
    

main()