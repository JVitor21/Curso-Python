"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = 'Olá mundo'
print(len(variavel))# pega a variavel toda
print(variavel[0:len(variavel):1])# toda a palavra incluindo espaços
print(variavel[0:9:2])# de dois em dois caracteres incluindo espaços
print(variavel[-1:-10:-1])  # de trás para frente incluindo espaços
