import six
import sys
sys.modules['sklearn.externals.six']=six
import mlrose


pessoas=[('Lisboa', 'LIS'),
        ('Madrid', 'MAD'),
        ('Paris', 'CDG'),
        ('Dublin', 'DUB'),
        ('Bruxelas', 'BRU'),
        ('Londres', 'LHR')]
destino='FC0'

voos={}

with open('C:/Users/camil/OneDrive/Desktop/CURSO IA/MODULO 2/flights.txt')as file:
    for linha in file:
        origem, destino, saida, chegada, preco=linha.split(',')
        voos.setdefault((origem, destino), [])
        voos[(origem, destino)].append((saida, chegada, int(preco)))
        

def calcular_preco(agenda):
    total_preco=0
    id_voo=-1
    for i in range(len(agenda)//2):
        origem=pessoas[i][1]
        id_voo+=1
        ida=voos[(origem,destino)][agenda[id_voo]]
        total_preco+=ida[2]
        id_voo+=1
        volta = voos[(destino,origem)][agenda[id_voo]]
        total_preco+=volta[2]
    return total_preco
def imprimir_voos(agenda):
    total_preco=0
    id_voo=-1
    for i in range(len(agenda)//2):
        nome=pessoas[i][0]
        origem=pessoas[i][1]
        id_voo+=1
        ida=voos[(origem,destino)][agenda[id_voo]]
        total_preco+=ida[2]
        id_voo+=1
        volta=voos[(destino,origem)][agenda[id_voo]]
        total_preco+=volta[2]
        print('%10s%10s %5s-%5s %3s %5s-%5s %3s' % (nome, origem, ida[0], ida[1], ida[2], volta[0], volta[1], volta[2]))
    print("Total do Preço: ", total_preco)
fitness=mlrose.CustomFitness(calcular_preco)

problema= mlrose.DiscreteOpt(length=12,fitness_fn=fitness, maximize=False, max_val=10)

melhor_solucao, menor_preco = mlrose.hill_climb(problema)
print(melhor_solucao)
imprimir_voos(melhor_solucao)



       