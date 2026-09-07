# Trabalhe com um dos programas dos exercícios 3.4 a 3.7

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

print("Pessoal, eu encontrei uma mesa maior, irei convidar mais três pessoas\n")

convidados.insert(0, 'Freddie Mercury')

convidados.insert(2, 'Jimi Hendrix')

convidados.append('Michael Jackson')

print("========Nova Lista de Convidados========")
for pessoa in convidados:
    print(pessoa + message)

# Use len() para exibir uma mensagem informando o número de pessoas que está convidando para o jantar
print("Número de convidados: ", len(convidados))