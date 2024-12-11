"""
Lists em Python
Tipo list - Mutável
Suporta vàrios valores de qualquer tipo
Conhecimentos reutilizaveis - indices e fatiamento
Métodos uteis: append, insert, pop, del, clear, extend, +
"""
#      +01234 (indice positivo) 
#      -54321 (indice negativo)
# para acessar o elemento utiliza o [], ex: [3] acessa o 3
string = 'ABCDE' # 5 caraceteres (len para checar o tamanho ou quantidade de caractere)
#         0     1        2          3
#        -5    -4       -3         -2          
lista = [123, True, 'Luiz Otávio', 1.2, 
         [321, False, 'João Vitor', 2.1, []]] # ou list() posso por uma lista dentro de outra
lista_2 = [456, True, 'Ashilly', 45.5]
# print(bool([])) # false
lista[-3] = 'Maria'
print(lista)
print(lista[2], type(lista[2]))
# print(f'Lista 1 :{lista} \n', 
#       f'Lista 2: {lista_2}')