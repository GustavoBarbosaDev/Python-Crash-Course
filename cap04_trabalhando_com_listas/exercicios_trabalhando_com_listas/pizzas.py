# Pense em pelo menos 3 tipos de pizza
# Armazene os nomes e utilize um laço for para exibir o nome de cada pizza
pizzas = ['calabresa', 'frango com catupiry', 'carne de sol']

print("\n========Sabores de pizzas========")
for pizza in pizzas:
    print(pizza)

# Modifique o laço for para mostrar uma frase usando o nome da pizza em vez de exibir apenas o nome dela. 
print("\n========Frases com Pizzas========")
for pizza in pizzas:
    print("Eu amo pizza de " + pizza)

# Acrescente uma linha final de seu programa, fora do laço for, que informe quanto você gosta de pizza.
print("\nEu realmente amo esses sabores de pizza!")