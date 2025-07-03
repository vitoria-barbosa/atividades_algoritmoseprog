# 1 1 1
# 1 2 2
# 2 4 8
# 2 5 9
# 3 9 27
# 3 10 28
# 4 16 64
# 4 17 65
# 5 25 125
# 5 26 126
def main():
    n = int(input())
    a = 1
    b = 1
    c = 1
    for i in range(n):
        print(f"{a}, {b}, {c}")
        print(f"{a}, {b+1}, {c+1}")

        a += 1
        b = a ** 2
        c = a ** 3

main()