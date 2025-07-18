def main():
    array = []

    v = int(input())

    for i in range(10):
        array.append(v)
        print(f"N[{i}] = {v}")

        v *= 2

main()