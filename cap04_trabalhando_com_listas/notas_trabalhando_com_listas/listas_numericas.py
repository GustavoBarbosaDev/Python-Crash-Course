# Existem muitos motivos para armazenar um conjunto de números. Em visualizações de dados, quase sempre se trabalha com um
# conjunto de números, como temperaturas, distâncias, tamanhos de população ou valores de latitude e longitudes
# As listas são ideais para armazenar conjuntos de números e Python oferece várias ferramentas para ajudar a trabalhar com
# listas de números de forma eficiente

# A função range() de Python facilita gerar uma série de números. 
# Ela pode ser usada para exibir uma sequência de números de 1 à 4
for value in range(1,5):
    print(value)
# A função range() faz Python começar a contar no primeiro valor fornecido e parar quando atingir o segundo valor especificado
# Como ele para no segundo valor definido, a saída não conterá o valor final 5

# É possível converter diretamente os resultados de range() em uma lista usando a função list()
# Quando list() é colocado em torno de uma chamada à função range(), a saída é uma lista de números
numbers = list(range(1,6))
print(numbers)

# Também é possivel usar range() para dizer a Python que ignore alguns números em um dado intervalo
even_numbers = list(range(2,11,2))
print(even_numbers)
# Nesse exemplo a função range() começa com o 2 e então soma 2 a esse valor. Essa soma vai se repetir até o valor final 11 
# ser ultrapassado