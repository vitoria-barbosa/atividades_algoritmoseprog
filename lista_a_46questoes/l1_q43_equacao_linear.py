def principal():
    a = int(input('Digite um valor inteiro para A: '))
    b = int(input('Digite um valor inteiro para B: '))
    c = int(input('Digite um valor inteiro para C: '))
    d = int(input('Digite um valor inteiro para D: '))
    e = int(input('Digite um valor inteiro para E: '))
    f = int(input('Digite um valor inteiro para F: '))

    x = ((c*e) - (b*f)) / ((a*e) - (b*d))
    y = ((a*f) - (c*d)) / ((a*e) - (b*d))
    print(f'Levando em consideração os valores fornecidos, x={x:.2f} e y={y:.2f}')

principal()
