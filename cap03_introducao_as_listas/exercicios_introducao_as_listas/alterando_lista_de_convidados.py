# Um dos convidados não poderá comparecer ao jantar, portanto será necessário enviar um novo conjunto de convites

# Comece com o programa do Exercício lista_de_convidados.py
convidados = ['George Harrison', 'John Lennon', 'Paul McCartney', 'Ringo Starr']

message = ", você está convidado para um jantar muito especial, traga seu instrumento musical favorito!\n"

print("========Lista de Convidados========")
for pessoa in convidados:
    print(pessoa + message)

# Acrescente um print, especificando o nome do convidado que não poderá comparecer
print("========Imprevisto========")
print(convidados[1] + " não poderá comparecer\n")

# Modifique a lista, substituindo o nome do convidado que não poderá comparecer pela nova pessoa a ser convidada
convidados[1] = 'Robert Plant'

# Exiba um segundo conjunto de mensagens com o convite, uma para cada pessoa que continua presente na lista
print("========Lista com novo convidado========")
for pessoa in convidados:
    print(pessoa + message)