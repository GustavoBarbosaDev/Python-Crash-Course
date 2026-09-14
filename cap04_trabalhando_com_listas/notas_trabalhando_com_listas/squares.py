# Lista dos dez primeiros quadrados perfeitos com range().
# Em Python, dois asteriscos (**) representam exponenciação.

squares = []                        # O programa começa com uma lista vazia
for value in range(1, 11):          # Dizemos para Python percorrer cada valor de 1 a 10 usando range().
    square = value**2               # O valor atual é elevado ao quadrado e armazenado na variável square
    squares.append(square)          # Cada novo valor é adicionado à lista squares.

print(squares)                      # Por fim a lista é exibida

# Outra maneira de fazer seria concatenando cada novo valor diretamente na lista
# squares.append(value**2)

# Algumas funções em Python são específicas para listas de números
# Para encontrar o valor mínimo
print(min(squares))
# Para encontrar o valor máximo 
print(max(squares))
# Para somar todos os itens de uma lista
print(sum(squares))

# Uma list comprehension permite criar uma lista com apenas uma linha de código, combinando um laço for com a criação de
# novos elementos e adicionando cada elemento automaticamente.

# Criando a lista squares com list comprehension
squares2 = [value**2 for value in range(1, 11)]
print(squares2)
