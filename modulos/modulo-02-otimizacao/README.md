# ⚙️ Módulo 2: Otimização e Algoritmos Genéticos

## Descrição

Implementações de técnicas de otimização combinatória usando algoritmos meta-heurísticos, com foco em **MLRose** e problemas reais de agendamento.

## Arquivos

### 1. `mlrose.py`
**Biblioteca:** MLRose (Machine Learning, Randomized Optimization and SEarch)

**Descrição:**
- Implementação de algoritmos de otimização
- Algoritmos Genéticos
- Hill Climbing
- Simulated Annealing
- MIMIC (Mutual Information Maximizing Input Clustering)

**Algoritmos implementados:**
- **Algoritmos Genéticos:** Evolução de população de soluções
- **Hill Climbing:** Busca local gulosa
- **Simulated Annealing:** Busca com aceitação probabilística de piora
- **Random Hill Climbing:** Hill Climbing com reinicializações

### 2. `flights.txt`
**Problema:** Agendamento de Voos

**Descrição:**
- Dados de disponibilidade de voos entre cidades
- Problema de otimização combinatória
- Objetivo: Minimizar custo total e tempo de viagem
- Restrições: Horários disponíveis, escalas, preferências

**Exemplo de aplicação:**
- Planejamento de viagens corporativas
- Otimização de rotas aéreas
- Minimização de custos de transporte

### 3. `exercicio1.py` e `Exercício2.py`
Exercícios práticos de aplicação de algoritmos de otimização.

## Conceitos Teóricos

### Algoritmos Genéticos

**Inspiração:** Seleção natural e evolução biológica

**Componentes:**
1. **População:** Conjunto de soluções candidatas
2. **Fitness:** Função que avalia qualidade da solução
3. **Seleção:** Escolha dos "pais" mais aptos
4. **Crossover:** Combinação de características dos pais
5. **Mutação:** Introdução de variações aleatórias

**Pseudocódigo:**
```
1. Inicializar população aleatória
2. Avaliar fitness de cada indivíduo
3. ENQUANTO critério de parada não for atingido:
    a. Selecionar pais
    b. Aplicar crossover
    c. Aplicar mutação
    d. Avaliar fitness da nova geração
    e. Substituir população antiga
```

### Hill Climbing

**Descrição:**
- Algoritmo de busca local
- Sempre escolhe vizinho com melhor fitness
- Pode ficar preso em ótimos locais

**Variantes:**
- **Steepest Ascent:** Avalia todos os vizinhos
- **First-Choice:** Escolhe primeiro vizinho melhor
- **Random Restart:** Reinicia de pontos aleatórios

### Simulated Annealing

**Inspiração:** Processo de recozimento de metais

**Características:**
- Aceita soluções piores com probabilidade decrescente
- Temperatura controla aceitação de piora
- Evita ótimos locais explorando mais no início

**Função de aceitação:**
```python
prob = exp(-(custo_novo - custo_atual) / temperatura)
if random() < prob:
    aceitar_solucao_pior()
```

## Comparação de Algoritmos

| Algoritmo | Vantagens | Desvantagens | Melhor para |
|-----------|-----------|--------------|-------------|
| **Algoritmo Genético** | Explora espaço amplo, robusto | Lento, muitos parâmetros | Problemas complexos |
| **Hill Climbing** | Rápido, simples | Ótimos locais | Espaços convexos |
| **Simulated Annealing** | Evita ótimos locais | Configuração de temperatura | Médio porte |
| **Random Restart HC** | Balanceia exploração | Vários restarts | Múltiplos ótimos |

## Como Executar

```bash
# Instalar dependências
pip install mlrose numpy

# Executar otimização com MLRose
python mlrose.py

# Problema de agendamento de voos
python exercicio1.py

# Exercícios avançados
python Exercício2.py
```

## Exemplo de Uso

### Algoritmo Genético com MLRose

```python
import mlrose

# Definir problema (exemplo: Traveling Salesman)
fitness = mlrose.TravellingSales(coords=[(0,0), (1,1), (2,2)])
problem = mlrose.TSPOpt(length=3, fitness_fn=fitness, maximize=False)

# Configurar Algoritmo Genético
best_state, best_fitness = mlrose.genetic_alg(
    problem,
    pop_size=200,
    mutation_prob=0.1,
    max_attempts=100
)

print(f"Melhor solução: {best_state}")
print(f"Fitness: {best_fitness}")
```

### Hill Climbing

```python
# Hill Climbing
best_state, best_fitness = mlrose.hill_climb(
    problem,
    max_attempts=100,
    restarts=10
)
```

### Simulated Annealing

```python
# Simulated Annealing
schedule = mlrose.ExpDecay()
best_state, best_fitness = mlrose.simulated_annealing(
    problem,
    schedule=schedule,
    max_attempts=100
)
```

## Problemas Clássicos

### 1. Traveling Salesman Problem (TSP)
Encontrar menor rota visitando todas as cidades uma vez.

### 2. Knapsack Problem
Maximizar valor de itens em uma mochila com capacidade limitada.

### 3. Job Scheduling
Agendar tarefas minimizando tempo total ou custos.

### 4. N-Queens Problem
Posicionar N rainhas em tabuleiro sem ataques.

## Parâmetros Importantes

### Algoritmo Genético
- **pop_size:** Tamanho da população (100-500)
- **mutation_prob:** Probabilidade de mutação (0.05-0.2)
- **crossover_prob:** Probabilidade de crossover (0.7-0.9)
- **max_attempts:** Tentativas sem melhoria (10-100)

### Simulated Annealing
- **schedule:** Cronograma de resfriamento
- **max_attempts:** Iterações máximas
- **temperature inicial:** Controla exploração

## Referências

- [MLRose Documentation](https://mlrose.readthedocs.io/)
- Holland, J. H. - *Adaptation in Natural and Artificial Systems*
- Kirkpatrick, S., Gelatt, C. D., & Vecchi, M. P. - *Optimization by Simulated Annealing*
