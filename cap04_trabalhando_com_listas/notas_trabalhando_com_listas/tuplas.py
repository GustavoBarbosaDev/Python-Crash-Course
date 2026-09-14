# Tuplas são listas imutáveis definidas exatamente como listas, porêm com parênteses no lugar dos colchetes
# Depois de definidas, podemos acessar seus elementos individuais da mesma forma que é feita em listas

# Exemplo
# Um retângulo que têm sempre determinado tamanho
dimensions = (200, 50) # Essa tupla garante que o tamanho desse retângulo não mudará
print(dimensions[0])
print(dimensions[1])

# Ao tentar mudar um valor dentro de uma tupla, Python retornará um erro de tipo. 
# dimensions[0] = 250

# Podemos percorer todos os valores de uma tupla usando o laço for, assim como em listas
for dimension in dimensions:
    print(dimension)

# Embora não seja possível modificar uma tupla, é possível atribuir um novo valor a uma variável que armazena uma tupla, 
# podendo assim redefinir a tupla toda

print("\nDimensões Originais:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nDimensões modificadas:")
for dimension in dimensions:
    print(dimension)

# Python não gera nenhum erro, pois sobrescrever uma variável é uma operação válida