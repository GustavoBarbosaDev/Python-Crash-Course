# Crie uma lista de números de um a um milhão 
milhao = []

for numero in range(1,1000001):
    milhao.append(numero)

# Use min() e max() para garantir que a lista realmente comece em um e termine em um milhão
print(min(milhao))
print(max(milhao))

# Utilize a função sum() para ver a rapidez com que Python é capaz de somar um milhão de números
print(sum(milhao))