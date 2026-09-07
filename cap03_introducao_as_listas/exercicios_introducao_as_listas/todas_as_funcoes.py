# Pense em algo que você poderia armazenar em uma lista. Escreva um programa que crie uma lista contendo itens e então 
# utilize cada função apresentada no capítulo pelo menos uma vez

print("Preciso listar as minhas compras")
compras = ['limão', 'sabão', 'arroz', 'feijão']
print(compras)

print("Vovó disse para eu comprar uma esponja também, como ela fica na mesma sessão do sabão irei coloca-la ao lado dele na lista")
compras.insert(2, 'esponja')
print(compras)

print("Mamãe disse que o primeiro item da lista já tem o suficiente, então terei de remove-lo")
del compras[0]
print(compras)

print("Minha tia disse que já está levando o último item da lista, então posso remover")
compras.pop()
print(compras)

print("Meu avô quer fazer churrasco, então preciso adicionar carne, carvão, toscana e óleo ao final da lista")
compras.append('carne')
compras.append('carvão')
compras.append('toscana')
compras.append('óleo')
print(compras)

print("Mamãe falou que acabou de encontrar um pacote de esponjas, mas não sei a posição dele na lista")
compras.remove('esponja')
print(compras)

print("Ótimo, agora posso me organizar melhor. Portanto irei organizar em ordem alfabética temporariamente, para ver como fica")
print(sorted(compras))

print("Acho que agora posso definir a lista em ordem alfabética")
compras.sort()
print(compras)

print("Na verdade, preciso economizar tempo, e percebi que a melhor ordem pode ser a inversa, então alterarei a ordem da lista")
compras.reverse()
print(compras)