# É possível trabalhar com um grupo específico de itens de uma lista, que Python chama de fatia.
# Para criar uma fatia, é preciso especificar o índice do primeiro e do último elemento com os quais deseja trabalhar.
jogadores = ['rossi', 'royal','pereira', 'ortiz', 'ayrton', 'jorginho', 'pulgar', 'arrascaeta', 'lino', 'pedro', 'carrascal']
print(jogadores[0:3])   # Os elementos de índice 0, 1 e 2 serão devolvidos
# A saída mantém a estrutura de lista e inclui os três primeiros jogadores
# É possível gerar qualquer subconjunto de uma lista
print("Linha de defesa: ", jogadores[1:5])
print("Linha de meio-campo: ", jogadores[5:8])
print("Linha de ataque: ", jogadores[8:11])

# Se o primeiro índice de uma fatia for omitido, Python começa a fatia automaticamente no início da lista.
print("11 em campo: ", jogadores[:11])

# De forma semelhante, se o último índice for omitido, Python inclui todos os elementos até o final da lista.
print("11 em campo: ", jogadores[0:])

# Essa sintaxe permite apresentar todos os elementos a partir de qualquer ponto da lista até o final.
# Índices negativos contam a partir do final da lista.
print("Últimos três jogadores: ", jogadores[-3:])

# É possível usar uma fatia em um laço for para percorrer um subconjunto de elementos de uma lista

for jogador in jogadores[:3]:       # Python percorre somente os três primeiros nomes da lista
    print(jogador.title())