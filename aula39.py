"""
Iterando strings com while
"""
#       012345678910
nome = input("Digite seu nome: ") # Iteráveis
#    -10-9-8-7-6-5-4-3-2-1
# print(nome[-10])
# tamanho_nome = len(nome)
# print(nome)
# print(tamanho_nome)
novo_nome = ""
indice = 0

while indice < len(nome):
    novo_nome += nome[indice] + "*"
    indice += 1
print(novo_nome)