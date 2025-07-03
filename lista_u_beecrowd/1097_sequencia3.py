# I=1 J=7
# I=1 J=6
# I=1 J=5
# I=3 J=9
# I=3 J=8
# I=3 J=7

# ...
# I=9 J=15
# I=9 J=14
# I=9 J=13
def main():
    i = 1
    j = 7
    

    while i <= 9:
        contador = 0
        j_aux = j
        while contador < 3:
            print(f"I={i} J={j_aux}")
            j_aux -= 1
            contador += 1
        j += 2
        i += 2


main()