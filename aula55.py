"""
Introdução ao desempacotamento + tiples (tuplas)
"""
# nomes = ['Maria', 'Helena', 'Luiz']
nome1, nome2, nome3 = ['Maria','Helena','Luiz'] # desempacota
nome1, *resto = ['Maria','Helena','Luiz'] # empacota
nome1, *_ = ['Maria','Helena','Luiz'] # empacota
_ , _ , nome, *_ = ['Maria','Helena','Luiz'] # empacota

print(nome,'\nlista com o resto: ', _)