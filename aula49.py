"""
Lists em Python
Tipo list - Mutável
Suporta vàrios valores de qualquer tipo
Conhecimentos reutilizaveis - indices e fatiamento
Métodos uteis: append, insert, pop, del, clear, extend, +
Create Read Update Delete
Criar, ler, alterar, apagar = list[i] (CRUD)
"""
#         0   1   2   3   4   5
#         -6  -5 -4   -3  -2  -1
lista = [ 10, 20, 30, 40, 50, 60]
# lista[2] = 300
# del lista[2]
# print(lista[2])
lista.append(70) #adiciona mais 1 ao final da lista
lista.pop() 
lista.append(80)
lista.append('BBB')
# remove o ultimo item adicionado ate o momento da execução do metodo
ultimo_valor = lista.pop(3) # Evitar mexer no meio da lista se ela for grande
print(lista, 'Removido,', ultimo_valor)