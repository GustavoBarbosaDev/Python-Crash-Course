# Crie uma lista de números de um a um milhão e, então, use um laço for para exibir os números
milhao = []

for numero in range(1, 1000001):
    milhao.append(numero)

for numero in milhao:
    print(numero)