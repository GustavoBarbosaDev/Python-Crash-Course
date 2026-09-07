# Crie uma lista que inclua pelo menos três pessoas das quais gostaria de convidar para jantar. Em seguida, utilize uma 
# lista para exibir uma mensagem para cada pessoa, convidando-a para jantar.

convidados = ['George Harrison', 'John Lennon', 'Paul McCartney', 'Ringo Starr']

message = ", você está convidado para um jantar muito especial, traga seu instrumento musical favorito!\n"

for pessoa in convidados:
    print(pessoa + message)