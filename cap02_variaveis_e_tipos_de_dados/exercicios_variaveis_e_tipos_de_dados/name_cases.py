# Armazene o nome de uma pessoa em uma variável e apresente uma mensagem a essa pessoa
name = "Junin do Gás"
print("Olá " + name + " é um prazer te conhecer")

# Armazene o nome de uma pessoa em uma variável e então apresente o nome dessa pessoa em letras minúsculas, em letras maiúsculas e somente com a primeira letra maiúscula
name2 = "GIorGiAN De arRAsCaETa"
print(name2.lower()) # Exibe com todas as letras minúsculas
print(name2.upper()) # Exibe com todas as letras maiúsculas
print(name2.title()) # Exibe com a primeira letra maiúscula

# Encontre uma citação de uma pessoa famosa que você admire. Exiba a citação e o nome do autor. Sua saída deverá ter a aparẽncia a seguir, incluindo as aspas:
# Albert Einstein certa vez disse: "Uma pessoa que nunca cometeu um erro jamais tentou nada novo."
print('Malcom X certa vez disse: "A educação é o nosso passaporte para o futuro, pois o amanhã pertence às pessoas que se preparam hoje."')

# Repita o exercício anterior, porém, desta vez, armazene o nome da pessoa famosa em uma variável chama famous_person
# Em seguida, componha sua mensagem e armazene-a em uma nova variável chamada message. Exiba sua mensagem.
famous_person = "Malcom X"
message = '"A educação é o nosso passaporte para o futuro, pois o amanhã pertence às pessoas que se preparam hoje."'
print(famous_person + " certa vez disse: " + message)

# Armazene o nome de uma pessoa e inclua alguns caracteres em branco no início e no final do nome.
# Lembre-se de usar cada combinação de caracteres, "\t" e "\n" pelo menos uma vez
# Exiba o nome uma vez, de modo que os espaços em branco em torno do nome sejam mostrados.
# Em seguida, exiba o nome usando cada uma das três funções de remoção de espaços: lstrip(), rstrip() e strip()

name3 = " Gustavo "
print("\t" + name3 + "\n\t" + name3.lstrip() + "\n\t" + name3.rstrip() + "\n\t" + name3.strip())

