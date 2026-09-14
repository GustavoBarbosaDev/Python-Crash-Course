# Um restaurante oferece apenas cinco tipos básicos de comida
# Pense em 5 pratos simples e armazene-os em uma tupla
pratos = ('omelete', 'macarrão', 'frango com legumes', 'calabresa acebolada', 'purê de batata')

# Use um laço for para exibir cada prato oferecido pelo restaurante
print("Cardápio:")
for prato in pratos:
    print(prato)

# Tente modificar um dos itens e certifique-se de que Python rejeite a mudança 
# pratos[1] = 'macarronada'
# Erro Gerado:
# Traceback (most recent call last):
#  File "/home/gustavobarbosa/Documents/GitHub/Python-Crash-Course/cap04_trabalhando_com_listas/exercicios_trabalhando_com_listas/buffet.py", line 11, in <module>
#    pratos[1] = 'macarronada'
#    ~~~~~~^^^
# TypeError: 'tuple' object does not support item assignment

# O restaurante mudou o cardápio, substituindo dois dos itens com pratos diferentes
# Acrescente um bloco de código que reescreva a tupla 
pratos = ('ovos mexidos', 'macarronada', 'frango empanado', 'bife acebolado', 'batata frita')

# Use um laço for para exibir cada item do cardápio revisado
print("\nCardápio modificado: ")
for prato in pratos:
    print(prato)