# I=1 J=60
# I=4 J=55
# I=7 J=50
# ...
# I=? J=0
def main():
    i = 1
    j = 60

    while j >= 0:
        print(f"I={i} J={j}")
        i += 3
        j -= 5

main()