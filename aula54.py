"""
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""
print('Minha solução:')

lista = ['Maria', 'Helena', 'Luiz']
indice_1 = 0
lista.append('João Vitor')
lista.insert(0, 'Pedro')

for nome in lista:
    nome = lista[indice_1]
    print(indice_1, nome, type(nome))
    indice_1 += 1

print('\nSolução do professor:')

lista_2 = ['Fernando', 'Paulo', 'Hugo']
lista_2.append('Jorge')
lista_2.insert(1, 'Julia')
indices = range(len(lista_2))

for indice in indices:
    print(indice, lista_2[indice], type(lista_2[indice]) )