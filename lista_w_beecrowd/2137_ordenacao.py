def main():

    while True:
        try:
            casos = int(input())
            livros = []

            for _ in range(casos):
                livro = int(input())
                livros.append(livro)
            
            livros_ordenados = sorted(livros)

            for i in range(casos):
                print(str(livros_ordenados[i]).zfill(4))

        except EOFError:
            break

main()