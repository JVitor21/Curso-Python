"""while/else"""
string = 'Valor qualquer'

i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ':
        break

    print(letra)
    i += 1
else:
    print('\nNão encontrei um espaço vazio na string.')
print('Fora do while.')