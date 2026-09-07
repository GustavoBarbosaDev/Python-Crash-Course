# A mesa de jantar maior não chegará a tempo para o jantar e tem espaço para somente dois convidados

# Comece com o programa do exercício mais_convidados.py
convidados = ['George Harrison', 'John Lennon', 'Paul McCartney', 'Ringo Starr']

message = ", você está convidado para um jantar muito especial, traga seu instrumento musical favorito!"

print("\n========Lista de Convidados========")
for pessoa in convidados:
    print(pessoa + message)

print("\n========Imprevisto========")
print(convidados[1] + " não poderá comparecer")

convidados[1] = 'Robert Plant'

print("\n========Lista com novo convidado========")
for pessoa in convidados:
    print(pessoa + message)

print("\n========Mesa nova encontrada========")

print("Pessoal, eu encontrei uma mesa maior, irei convidar mais três pessoas")


convidados.insert(0, 'Freddie Mercury')


convidados.insert(2, 'Jimi Hendrix')


convidados.append('Michael Jackson')

print("\n========Nova Lista de Convidados========")
for pessoa in convidados:
    print(pessoa + message)

# Acrescente uma nova linha para mostrar uma mensagem informando que só pode convidar duas pessoas para o jantar
print("\n========Mais um imprevisto========")
print("Aconteceu mais um imprevisto, a mesa não vai chegar a tempo, então só dois de vocês vão ficar, o resto vai rapar fora!\n")

# Utilize pop() para remover os convidados da lista, um de cada vez, até que apenas dois nomes apareçam na lista. Sempre
# que remover um nome da lista, mostre uma mensagem para a pessoa, permitindo que ela saiba que sente muito por não poder
# convidá-la para jantar
print("\n========Desconvidando========")
print(convidados.pop() + ", sinto muito, você está desconvidado do jantar.")
print(convidados.pop() + ", sinto muito, você está desconvidado do jantar.")
print(convidados.pop() + ", sinto muito, você está desconvidado do jantar.")
print(convidados.pop() + ", sinto muito, você está desconvidado do jantar.")
print(convidados.pop() + ", sinto muito, você está desconvidado do jantar.")

# Apresente uma mensagem para cada uma das duas pessoas qua ainda estão na lista, permitindo que elas saibam que ainda estão
# convidadas
print("\n========Avisando quem ainda está convidado========")
for pessoa in convidados:
    print(pessoa + ", você ainida está convidado, venha jantar!")

# Utilize del para remover os dois últimos nomes da lista, de modo que tenha uma lista vazia
del convidados[0]
del convidados[0]

# Mostre a lista para garantir que realmente tem uma lista vazia no final do programa.
print("\n========Lista Vazia========")
print(convidados)
