# Leia um valor inteiro X. Em seguida apresente os 6 valores ímpares consecutivos a partir de X, um valor por linha, inclusive o X ser for o caso.
def main():
    x = int(input())
    contador = 0
    
    while contador < 6:
        if not x % 2 == 0:
            print(x)
            contador += 1
            
        x += 1
        

main()