# As listas são coleções de itens em uma ordem em particular que permitem armazenar conjuntos de informações em um só lugar
# É possível colocar qualquer informação em uma lista, e os itens não precisam estar relacionados de nenhum modo particular
# Em Python, colchetes([]) indicam uma lista, e elementos individuais da lista são separados por vírgulas

beatles = ['John Lennon', 'Paul McCartney', 'George Harrison', 'Ringo Star']
print(beatles) # Ao pedir que Python exiba uma lista, ele devolverá a representação da lista, incluindo os colchetes

# As listas são coleções ordenadas, portanto é possível acessar qualquer elemento de uma lista informando a posição ou índice
# do item desejado ao interpretador Python
# Para isso é preciso escrever o nome da lista seguido do índice do item entre colchetes

print(beatles[0]) # saída limpa, formatada de modo elgante

# A posição dos índices começa em 0, não em 1. O Python considera que o primeiro item de uma lista está na posição 0, e não
# na posição 1. Então sempre que quiser um item subtraia um de sua posição na lista

print(beatles[1]) # retorna o segundo item da lista
print(beatles[3]) # retorna o quarto item da lista

# Python sempre devolve o último item da lista quando o índice é -1. Essa sintaxe é bem útil quando se quer acessar os últimos
# itens de uma lista sem saber exatamente o tamanho dela. Essa convenção se estente a outros valores negativos. O índice -2
# devolve o penúltimo item e o índice -3 devolve o antepenúltimo item

# É possível usar valores individuais de uma lista exatamente como qualquer outra variável. Por exemplo concatenar para criar
# uma mensagem com base no valor de uma lista

message = beatles[-1] + " era o baterista dos Beatles."
print(message)

# A maioria das listas são dinâmicas, o que significa que serão adicionados e removidos elementos dela à medida que o programa
# executar
# A sintaxe pra modificar um elemento é semelhante à sintaxe pra acessar um elemento de uma lista. Use o nome da lista seguido
# do índice do elemento que deseja modificar e forneça o novo valor para o item

print(beatles) # antes da modificação
beatles[0] = 'John e Yoko'
print(beatles) # após a modifiação

# É possível acrescentar um novo elemento em uma lista. Python oferece várias maneiras de acrescentar novos dados em listas
# existentes

# A maneira mais simples de acrescentar um novo elemento a uma lista é concatenar o item na lista. Quando um item é concatenado
# em uma lista, o novo elemento é acrescentado no final

frutas = ['banana', 'maçã', 'laranja', 'uva', 'pera']
print(frutas)

frutas.append('limão')
print(frutas)

# O método append() acrescenta 'limão' no final da lista sem afetar os outros elementos
# Esse método facilita na criação de listas dinâmicas, pois pode-se criar uma lista vazia e então acrescentar itens à lista
# usando uma série de instruções append()

legumes = []
legumes.append('cebola')
legumes.append('batata')
legumes.append('cenoura')
legumes.append('brócolis')

# Criar listas assim é muito comum, pois com frequência os dados de um usuário não serão conhecidos até que ele os armazene em
# um programa que esteja sendo executado. Para que os usuários tenham o controle, é definida uma lista vazia que armazenará os
# valores de entrada dos usuários, que serão concatenados à lista

# É possível também adicionar um novo elemento em qualquer posição da lista usando o método insert(). 
# Isso é feito especificando o índice do novo elemento e o valor do novo item

print(legumes) # Antes de inserir um novo valor
legumes.insert(2, 'beterraba')
print(legumes) # Após inserir um novo valor

# O método insert() abre um espaço na posição do índice indicado e armazena o novo valor nesse local. Essa operação desloca
# os demais valores da lista uma posição à direita

# Remover elementos ou um conjunto de elementos de uma lista pode ser feito de acordo com a posição na lista ou pelo valor
# Se a posição do item que deseja remover da lista for conhecida, a instrução del pode ser usada
superherois = ['batman', 'super-man', 'thor', 'homem-aranha', 'flash', 'hulk' ]
print(superherois)

del superherois[0] # Remove batman da lista
print(superherois)

# A instrução del permite remover um item de qualquer posição de uma lista, se souber qual o índice do item. Não é possível
# acessar o valor removido da lista após a instrução del ter sido usada
# Em determinados situações, é preciso usar o valor de um item depois de removê-lo de uma lista. Em uma aplicação web por 
# exemplo, remover um usuário da lista de membros ativos e então adicioná-lo a lista de membros inativos
# O método pop() remove o último item de uma lista, mas permite trabalhar com o item após a remoção.
viloes = ['coringa', 'lex luthor', 'loki', 'venom', 'flash reverso', 'abominavel']
print(viloes)

vilao_removido = viloes.pop() # Remove 'abominavel' da lista e armazena esse valor na variavel
print(viloes)
print(vilao_removido) 
# A saída revela que o valor 'abominavel' foi removido do final da lista e agora está armazenado na variável vilao_removido

# O método pop() também pode ser usado para remover um item de qualquer posição de uma lista se incluir o índice do item a 
# ser removido entre parênteses
primeiro_removido = viloes.pop(0) # Remove 'coringa' da lista

# Em que situação usar del ou pop():
# del: Quando quiser um item de uma lista e esse item não vai ser usado de modo algum
# pop(): Quando quiser usar um item à medida que for removido

# É possível também remover um item de acordo com o valor dele usando o método remove()
livros = ['O Processo', '1984', 'A metamorfose', 'Vidas Secas', 'Noite na Taverna']
print(livros)

livros.remove('A metamorfose') # O código diz a Python para descobrir em que lugar 'A metamorfose' aparece e remove-lo
print(livros)
# O método remove() também permite trabalhar com o valor que está sendo removido da lista. Armazena-se o valor a ser
# removido dentro de uma variável e essa variável será usada no método remove() para informar a Python que o valor dentro
# da variável será removido da lista. Assim o valor é removido da lista, mas continua armazenado na variável.

# Listas são criadas em uma ordem imprevisível, pois nem sempre se pode controlar a ordem em que os usuários fornecem seus
# dados. Python oferece várias maneiras de organizar listas de acordo com a situação

# O método sort() de Python faz com que seja relativamente fácil ordernar uma lista. Ele altera a ordem da lista de forma
# permanente

# Ordenando uma lista de marcas de carro em ordem alfabetica com o método sort()
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() 
print(cars)  

# Também pode ser feita a ordem inversa passando o argumento reverse=True ao método sort()
cars.sort(reverse=True)
print(cars)

# Para preservar a ordem original de uma lista, mas apresenta-la de forma ordenada, pode-se usar a função sorted()
print("Essa é a versão original da lista:")
print(cars)

print("\nEssa é a lista ordenada sem alterar a lista original:")
print(sorted(cars)) # Essa função também pode receber o argumento reverse=True

print("\nEssa é a lista original de novo:")
print(cars)

# Para inverter a ordem original de uma lista, pode-se usar o método reverse(). Esse método não reorganiza a ordem de uma
# lista, ele simplesmente inverte a ordem da lista permanentemente

print(cars)
cars.reverse()
print(cars)

# É possível descobrir facilmente o tamanho de uma lista usando a função len()
len(cars)