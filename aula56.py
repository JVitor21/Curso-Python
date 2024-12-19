"""
Tipo tupla - Uma lista imutável
"""
nomes = ['Helena', 'Maria', 'Luiz']
# nomes = 'Helena', 'Maria', 'Luiz' # isso é uma tupla
# nomes[1] = 'outro'
# _, _, nome, *resto = nomes
nomes = tuple(nomes) # converte uma lista em uma tupla
nomes = list(nomes) #conerte uma tupla em uma lista
print(nomes[-1])
print(nomes)
# print(nome)