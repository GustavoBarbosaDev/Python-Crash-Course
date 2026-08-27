# Os números são usados com muita frequência em programação
# Python trata números de várias maneiras diferentes, de acordo com o modo como são usados

# Inteiros
# É possível com inteiros em Python
# Somar(+)
2 + 3
# Subtrair(-)
3 - 2
# Multiplicar(*)
2 * 3
# Dividir(/)
3 / 2
# Em uma sessão de terminal, Python simplesmente devolve o resultado da operação
# Dois simbolos de multiplicação são usados em Python para representar exponenciais
3 ** 2 # Resultado: 9
3 ** 3 # Resultado: 27
10 ** 6 # Resultado: 1000000
# A linguagem Python aceita a ordem das operações, tornando possível fazer várias operações em uma expressão
2 + 3 * 4 # Resultado: 14
# É possível usar parênteses para modificar a ordem das operações para que Python avalie a expressão na ordem especificada
(2 + 3) * 4 # Resultado: 20
# Espaços em branco não tem nenhum efeito no modo como Python avalia as expressões, eles servem para aumentar a legibilidade

# Números de ponto flutuante (float)
0.1 + 0.1 # Resultado:  0.2
2 * 0.1 # Resultado: 0.2
# As vezes pode-se obter um número arbitrário de casas decimais como resposta
0.2 + 0.1 # Resultado: 0.30000000000000004
# Isso acontece porque Python tenta encontrar uma forma de representar o resultado do modo mais exato possível

# Usar o valor de uma variável númerica em uma mensagem é frequente
# Exemplo
# age = 23
# message = "Happy " + age + "rd Birthday!"
# print(message)
# Se executar esse código, ele gera um erro de tipo
# Isso significa que Python não é capaz de reconhecer o tipo de informação usada
# Quando usar inteiros em strings desse modo, é preciso especificar explicitamente para o Python que quer usar o inteiro como uma string
# Isso é possível envolvendo a variável com a função str(), que diz ao Python par representar valores que não são strings como strings
age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message)
# Com isso o Python converte o valor numérico 23 em uma string e exibe os caracteres 2 e 3 como parte da mensagem
