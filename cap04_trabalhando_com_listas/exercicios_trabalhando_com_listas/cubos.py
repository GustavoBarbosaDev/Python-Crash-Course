# Crie uma lista dos dez primeiros cubos
cubos = []

for numero in range(1,11):
    cubo = numero ** 3
    cubos.append(cubo)

# Use um laço for para exibir o valor de cada cubo
for numero in cubos:
    print(numero)
