import six
import sys
sys.modules['sklearn.externals.six'] = six
import mlrose

produtos = [('Refrigerador A', 0.751, 999.90),
            ('Celular', 0.0000899, 2911.12),
            ('TV 55', 0.400, 4346.99),
            ('TV 50', 0.290, 3999.90),
            ('TV 42', 0.200, 2999.00),
            ('Notebook A', 0.00350, 2499.90),
            ('Ventilador', 0.496, 199.90),
            ('Microondas A', 0.0424, 308.66),
            ('Microondas B', 0.0544, 429.90),
            ('Microondas C', 0.0319, 299.29),
            ('Refrigerador B', 0.635, 849.00),
            ('Refrigerador C', 0.870, 1199.89),
            ('Notebook B', 0.498, 1999.90),
            ('Notebook C', 0.527, 3999.00)]
espaco_dispovivel=3

def imprimir(solucao):


    for i in range(len(solucao)):
        if solucao[i]==1:
           print('%s - %s' % (produtos[i][0], produtos[i][2]))
def fitness_function(solucao):
    custo=0
    soma_espaco=0 
    for i in range (len(solucao)):
        if solucao[i]==1:
            custo+=produtos[i][2]
            soma_espaco+= produtos[i][1]
    if soma_espaco>espaco_dispovivel:
        custo=1
    return custo
#exemplos usando pacotes mlrose
fitness =mlrose.CustomFitness(fitness_function)
problema=mlrose.DiscreteOpt(length=14, fitness_fn=fitness,
                            maximize=True,max_val=2)
#1

melhor_solucao, melhor_custo = mlrose.hill_climb(problema)

#2

melhor_solucao, melhor_custo = mlrose.simulated_annealing(problema)

#3 Melhor solucao pra esse tipo de execicio
melhor_solucao, melhor_custo = mlrose.genetic_alg(problema,pop_size=500,mutation_prob=0.2)
print(melhor_custo,melhor_solucao)
imprimir(melhor_solucao)
