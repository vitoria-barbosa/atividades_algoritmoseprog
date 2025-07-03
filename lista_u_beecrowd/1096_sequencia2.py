# I=1 J=7
# I=1 J=6
# I=1 J=5
# I=3 J=7
# I=3 J=6
# I=3 J=5
# ...
# I=9 J=7
# I=9 J=6
# I=9 J=5
def main():
    i = 1
    j = 7

    while i <= 9:
        j = 7
        while j >= 5:
            print(f"I={i} J={j}")
            j -= 1
        i += 2


main()