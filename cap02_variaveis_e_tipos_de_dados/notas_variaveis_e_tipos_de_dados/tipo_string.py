# String é uma série de caracteres
# Tudo que estiver entre aspas(simples ou duplas) é considerada uma string em Python
name = "gustavo barbosa" # String

# Uma das tarefas mais simples de se fazer com string é mudar o tipo de letra usando métodos
# Um método é uma ação que Python pode executar em um dado.
# Todo método é seguido de um conjunto de parênteses, pois os métodos, com frequência, precisam de informações
# adicionais(fornecidas entre os parênteses) para realizar sua tarefa

# Usando o método title() 
print(name.title()) # exibe cada palavra com a letra maiúscula no início
# O ponto(.) após name em name.title() informa a Python que o método title() deve atuar na variável name

# Usando o método upper()
print(name.upper()) # exibe todas as letras em maiúsculo

# Usando o método lower()
print(name.lower()) # exibe todas as letras em minúsculo

# Combinação ou Concatenação de strings
first_name = "gustavo"
last_name = "barbosa"
full_name = first_name + " " + last_name # Python usa o símbolo de adição para combinar as variáveis e atribuir essa combinação como valor de uma nova variável

print(full_name)
print("Hello " + full_name.title())


# Acrescentando espaços em branco em strings com tabulações ou quebras de linha
# Em programação, espaços em branco se referem a qualquer caractere que não é mostrado, como espaços, tabulações e símbolos de fim de linha
# Espaços em branco podem organizar a saída de modo que ela seja mais legível aos usuários

# A combinação de caracteres \t acrescenta uma tabulação no texto
print("\tMensagem com tabulação")

# A combinação de caracteres \n acrescenta uma quebra de linha no texto
print("Mensagem\nCom\nQuebra\nde\nlinha")

# É possível combinar tabulações e quebras de linha em uma mesma string
# A string "\n\t" diz a Python para passar para uma nova linha e iniciar a próxima com uma tabulação
print("Linguagens de Programação:\n\tPython\n\tC\n\tJavaScript")

# Espaços em branco extras podem ser confusos em programas, pois o Python identifica e considera significativo, a menos que seja informado o contrário
# as strings 'python' e 'python ' são duas strings diferentes
# Python é capaz de encontrar espaços em branco dos lados direito e esquerdo de uma string

# O método rstrip() garante que não haja espaços em branco do lado direito de uma string.
name = "Gustavo "
print(name.rstrip())

# A remoção é temporária, se o valor for solicitado novamente sem o método
print(name)

# Para que a remoção seja permanente é necessário remover o espaço em branco com rstrip() e amrmazenar o valor de volta na variável original
# Esta é uma operação frequente em programação
name = name.rstrip()
print(name)

# O método lstrip() garante que não haja espaços em branco do lado direito de uma string
name = " Gustavo"
print(name.lstrip())

# O método strip() remove espaços em branco dos dois lados ao mesmo tempo
name = " Gustavo "
print(name.strip())

# No mundo real essas funções de remoção são mais usadas com mais frequência para limpar entradas de usuários antes de armazená-las em um programa

