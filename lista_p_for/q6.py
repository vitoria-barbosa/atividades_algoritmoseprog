# Tabuada
def main():
    input("Aperte <enter> para ver a tabuada do 1 ao 10.\n")

    for tabuada in range(1, 11, 1):
        for i in range(1, 11, 1):
            multiplicacao = tabuada * i
            print(f"{tabuada} x {i:2.0f} = {multiplicacao}")
        print("\n------------\n")

main()