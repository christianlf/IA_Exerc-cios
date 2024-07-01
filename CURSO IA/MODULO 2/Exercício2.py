import six
import sys
sys.modules['sklearn.externals.six'] = six
import mlrose

# Adiciona compatibilidade para a importação de six
sys.modules['sklearn.externals.six'] = six

# Definição dos dados das pessoas e voos
pessoas = [('Lisboa', 'LIS'),
           ('Madrid', 'MAD'),
           ('Paris', 'CDG'),
           ('Dublin', 'DUB'),
           ('Bruxelas', 'BRU'),
           ('Londres', 'LHR')]

destino = 'FCO'
voos = {}

# Leitura dos dados dos voos a partir de um arquivo
with open('C:/Users/camil/OneDrive/Desktop/CURSO IA/MODULO 2/flights.txt') as file:
    for linha in file:
        origem, destino, saida, chegada, preco = linha.split(',')
        voos.setdefault((origem, destino), [])
        voos[(origem, destino)].append((saida, chegada, int(preco)))
# Função para calcular o custo total dos voos


# Função para imprimir os detalhes dos voos
def imprimir_voos(agenda):
    id_voo = -1
    total_preco = 0
    for i in range(len(agenda)//2):
        nome = pessoas[i][0]
        origem = pessoas[i][1]
        id_voo += 1
        ida = voos[(origem, destino)][agenda[id_voo]]
        total_preco += ida[2]
        id_voo += 1
        volta = voos[(destino, origem)][agenda[id_voo]]
        total_preco += volta[2]
        print('%10s%10s %5s-%5s %3s %5s-%5s %3s' % (nome, origem, ida[0], ida[1], ida[2], volta[0], volta[1], volta[2]))
    print('Preço total: ', total_preco)

# Criação da função de fitness customizada
fitness = mlrose.CustomFitness(imprimir_voos)

# Definição do problema de otimização
problema = mlrose.DiscreteOpt(length=12, fitness_fn=fitness, maximize=False, max_val=10)

# Execução do algoritmo Hill Climb
melhor_solucao, melhor_custo = mlrose.hill_climb(problema)

# Impressão dos resultados
print("Melhor custo:", melhor_custo)
print("Melhor solução:", melhor_solucao)

# Exemplo de impressão dos voos com uma agenda específica

imprimir_voos(melhor_solucao)