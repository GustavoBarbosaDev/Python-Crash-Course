# Uma mesa de jantar maior foi encontrada, portanto agora tem meia espaço. Convide mais 3 pessoas para o jantar

# Comece com o programa do Exercício alterando_lista_de_convidados.py
convidados = ['George Harrison', 'John Lennon', 'Paul McCartney', 'Ringo Starr']

message = ", você está convidado para um jantar muito especial, traga seu instrumento musical favorito!\n"

print("========Lista de Convidados========")
for pessoa in convidados:
    print(pessoa + message)

print("========Imprevisto========")
print(convidados[1] + " não poderá comparecer\n")

convidados[1] = 'Robert Plant'

print("========Lista com novo convidado========")
for pessoa in convidados:
    print(pessoa + message)

print("========Mesa nova encontrada========")
# Acrescente uma instrução print no final do programa informando às pessoas que uma mesa maior foi econtrada
print("Pessoal, eu encontrei uma mesa maior, irei convidar mais três pessoas\n")

# Utilize insert() para adicionar um novo convidado ao início da lista
convidados.insert(0, 'Freddie Mercury')

# Utilize insert() para adicionar um novo convidado no meio da lista
convidados.insert(2, 'Jimi Hendrix')

# Utilize append() para adicionar um novo convidado ao final da lista
convidados.append('Michael Jackson')

# Exiba um novo conjunto de mensagens de convite, uma para cada pessoa que está na sua lista
print("========Nova Lista de Convidados========")
for pessoa in convidados:
    print(pessoa + message)
