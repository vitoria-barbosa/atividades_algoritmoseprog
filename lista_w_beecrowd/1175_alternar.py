def main():
    array = []

    for _ in range(20):
        x = int(input())
        array.append(x)

    array.reverse()

    for i in range(20):
        print(f"N[{i}] = {array[i]}")

main()