# Com frequência, é preciso criar uma lista nova com base em uma outra lista já existente
# Para copiar uma lista, podemos criar uma fatia que inclui a lista original inteira omitindo os índices([:])
# Isso diz a Python para criar uma lista que começar no primeiro item e termina no último, gerando uma cópia da lista toda

minhas_comidas = ['pizza', 'hamburguer', 'bolo', 'coxinha', 'bomba']
comidas_da_festa = minhas_comidas[:]  # Aqui armazenamos a cópia da lista dentro da variável

print(minhas_comidas)
print(comidas_da_festa)

# Para provar que realmente temos duas listas separadas, acrescentamos um novo alimento em cada lista 
minhas_comidas.append('cachorro-quente')
comidas_da_festa.append('esfirra')

print(minhas_comidas)
print(comidas_da_festa)