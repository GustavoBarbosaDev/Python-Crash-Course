# Comece com o programa de pizzas.py 
pizzas = ['calabresa', 'frango com catupiry', 'carne de sol']

print("\n========Sabores de pizzas========")
for pizza in pizzas:
    print(pizza)

print("\n========Frases com Pizzas========")
for pizza in pizzas:
    print("Eu amo pizza de " + pizza)

print("\nEu realmente amo esses sabores de pizza!")

# Faça uma cópia da lista pizzas e chame de friend_pizzas
friend_pizzas = pizzas[:]

# Adicione uma nova pizza à lista original
pizzas.append('napolitana')

# Adicione uma pizza diferente à lista friend_pizzas
friend_pizzas.append('portuguesa')

# Prove que existem duas listas diferentes 
# Exiba a mensagem "Minhas pizzas favoritas são: " em seguida use um laço for para exibir a primeira lista
print("\nMinhas pizzas favoritas são: ")
for pizza in pizzas:
    print(pizza)

# Exiba a mensagem "As pizzas favoritas do meu amigo são: " em seguida use um laço for para exibir a segunda lista
print("\nAs pizzas favoritas do meu amigo são: ")
for pizza in friend_pizzas:
    print(pizza)