for indice in range(1, 10):
    if indice == 2:
        print('i é 2, pulando...')
        continue

    if indice == 8:
        print('i é 8, seu else não executará')
        break

    for j in range(1, 3):
        print(indice, j)
else:
    print('For completo com sucesso!')