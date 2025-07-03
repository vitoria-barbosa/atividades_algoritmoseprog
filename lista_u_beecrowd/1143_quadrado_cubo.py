# 1 1 1
# 2 4 8
# 3 9 27
# 4 16 64
# 5 25 125
def main():
    n = int(input())

    for i in range(1, n+1):
        print(f"{i} {i**2} {i**3}")

main()