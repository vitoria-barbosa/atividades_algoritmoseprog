# I=0 J=1
# I=0 J=2
# I=0 J=3
# I=0.2 J=1.2
# I=0.2 J=2.2
# I=0.2 J=3.2
# .....
# I=2 J=?
# I=2 J=?
# I=2 J=?
def main():
    i = 0.0
    while i <= 2.0001:
        for k in range(3):
            j = i + 1 + k
            if round(i, 1) == int(i):
                print(f"I={int(i)} J={int(j)}")
            else:
                print(f"I={round(i,1):.1f} J={round(j,1):.1f}")
        i = round(i + 0.2, 1)

main()