# É comum percorrer todas as entradas de uma lista, executando a mesma tarefa em cada item.
# Para isso é possível usar o laço for de Python.

# Percorrendo os 5 primeiros times do Brasileirão 2026
brasileirao = ['flamengo', 'palmeiras', 'cruzeiro', 'mirassol', 'fluminense'] 

print("\n========Tabela Brasileirão Top 5 ========")
for time in brasileirao:    # Diz a Python para extrair cada item da lista e armazená-lo na variável time
    print(time)             # Diz a Python para exibir o nome que acabou de ser armazenado

# O interpretador repete essas linhas uma vez para cada item da lista. Esse código pode ser lido como: "Para cada time na
# lista, exiba o nome do time"
# A saída é uma exibição simples de cada time da lista.

# O conceito de laços é importante, pois é uma das maneiras mais comuns para o computador autimatizar tarefas repetitivas
# O interpretador repete todo o laço até o último valor da lista. Como não há mais valores na lista, Python passa para a 
# próxima linha do programa.
# O conjunto de passos será repetido, uma vez para cada item da lista, não importa quantos itens haja na lista.
# É conveniente escolher um nome significativo para a variável temporária, que represente um único item da lista. Essa
# convenção de nomenclatura ajuda a acompanhar a execução em cada item em um laço for

# É possível fazer praticamente tudo com cada item de um laço for
# Podemos por exemplo exibir uma mensagem para cada time da lista do brasileirão informando sua colocação
print("\n========Colocação========")
colocacao = 1
for time in brasileirao:
    print(time.title() + " ficou em " + str(colocacao) + "° lugar no campeonato")
    colocacao += 1

# A cada repetição deste laço o nome do time muda e a colocação também, pois ao final de cada repetição é acrescentado 1 ao
# valor da variável colocacao

# É possível escrever quantas linhas de código quiser dentro de um laço for, pois toda linha indentada após o laço está 
# dentro do laço

# Qualquer linha de código após o laço for que não estiver indentada será executada uma vez, sem repetição. Python usa 
# indentação para determinar se uma linha de código está conectada à linha antes dela e também deixar o código bem fácil de
# ler. Basicamente, Python usa espaços em branco para forçar a escritura de um código formatado de modo organizado, com uma
# estrutura  visual clara.
# Níveis de indentação ajudam a ter uma noção geral da organização do programa como um todo