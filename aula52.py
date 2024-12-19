"""
Cuidados com dados mutáveis
= - copiando o valor (imutáveis)
= - aponta o mesmo valor na memória (mutável)
"""
lista_a = ['Luiz', 'Maria', 1, True, 1.2]
# lista_b = lista_a #aqui vc aponta para o mesmo valor e recebe ele
lista_b = lista_a.copy() #aqui vc copia o valor

lista_a[0] = 'Qualquer coisa' # usando o 1° vc muda o valor de b junto, usando o segundo, não
print(lista_b)
print(lista_a)
