# Pense em pelo menos 5 lugares do mundo que gostaria de visitar

# Armazene as localidades em uma lista. Certifique-se de que a lista não esteja em ordem alfabética
lugares = ['Itália', 'japão', 'Austrália', 'Egito', 'França']

# Exiba a lista na ordem original
print(lugares)

# Use sorted() para exibir a lista em ordem alfabética, sem modificar a lista propriamente dita
print(sorted(lugares))

# Mostre que sua lista manteve sua ordem original exibindo-a
print(lugares)

# Utilize sorted() para exibir sua lista em ordem alfabética inversa sem alterar a ordem original da lista
print(sorted(lugares, reverse=True))

# Mostre que a lista manteve a ordem original exibindo-a novamente
print(lugares)

# Utilize reverse() para mudar a ordem da lista. Exiba a lista para mostrar que sua ordem mudou
lugares.reverse()
print(lugares) 

# Utilize reverse() novamente para mudar a ordem da lista. Exiba a lista para mostrar que a lista voltou à sua ordem original
lugares.reverse()
print(lugares)

# Utilize sort() para mudar a lista de modo que ela seja armazenada em ordem alfabética. Exiba-a para mostra a mudança
lugares.sort()
print(lugares)

# Utilize sort() para mudar a lista de modo que ela seja armazenada em ordem alfabética inversa. Exiba-a para mostrar a mudança
lugares.sort(reverse=True)
print(lugares)