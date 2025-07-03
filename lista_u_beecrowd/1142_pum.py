# 1 2 3 PUM
# 5 6 7 PUM
# 9 10 11 PUM
# 13 14 15 PUM
# 17 18 19 PUM
# 21 22 23 PUM
# 25 26 27 PUM
def main():
    n = int(input())
    contador = 0
    i = 1
    while contador < n:
        for k in range(i, i+3):
            print(k, end=" ")
        
        print("PUM")
        i += 4
        contador += 1

main()
