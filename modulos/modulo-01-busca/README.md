# 🔍 Módulo 1: Algoritmos de Busca

## Descrição

Implementações de algoritmos clássicos de busca em Inteligência Artificial, explorando técnicas de busca informada e não-informada.

## Arquivos

### 1. `BuscaGulosa.py`
**Algoritmo:** Busca Gulosa (Greedy Search)

**Descrição:**
- Algoritmo de busca informada que escolhe sempre o caminho que parece estar mais próximo do objetivo
- Utiliza função heurística para estimar distância até o objetivo
- Não garante solução ótima, mas é mais rápido que busca completa

**Quando usar:**
- Problemas onde velocidade é mais importante que optimalidade
- Quando heurística é confiável
- Espaço de busca muito grande

### 2. `Buscar_estrela1.py`
**Algoritmo:** Busca A* (A-Star Search)

**Descrição:**
- Algoritmo de busca informada que combina custo real + heurística
- Função de avaliação: f(n) = g(n) + h(n)
  - g(n) = custo do caminho do início até n
  - h(n) = estimativa heurística de n até objetivo
- Garante solução ótima se heurística for admissível

**Quando usar:**
- Quando precisa da solução ótima
- Jogos (pathfinding em mapas)
- Navegação GPS
- Planejamento de rotas

### 3. `exercicio1.py`
Exercícios práticos aplicando os conceitos de busca.

## Conceitos Teóricos

### Heurísticas
Funções que estimam o custo de alcançar o objetivo a partir de um estado.

**Tipos comuns:**
- **Distância Euclidiana:** `sqrt((x2-x1)² + (y2-y1)²)`
- **Distância Manhattan:** `|x2-x1| + |y2-y1|`
- **Distância Chebyshev:** `max(|x2-x1|, |y2-y1|)`

### Comparação de Algoritmos

| Algoritmo | Completo? | Ótimo? | Complexidade Tempo | Complexidade Espaço |
|-----------|-----------|--------|-------------------|---------------------|
| Busca Gulosa | Não | Não | O(b^m) | O(b^m) |
| A* | Sim | Sim* | O(b^d) | O(b^d) |

\* Se heurística for admissível

## Como Executar

```bash
# Busca Gulosa
python BuscaGulosa.py

# Busca A*
python Buscar_estrela1.py

# Exercícios
python exercicio1.py
```

## Exemplo de Uso

```python
# Exemplo de implementação de heurística
def heuristica_manhattan(estado, objetivo):
    return abs(estado[0] - objetivo[0]) + abs(estado[1] - objetivo[1])

# Exemplo de uso do A*
caminho = busca_a_estrela(inicio, objetivo, heuristica_manhattan)
```

## Referências

- Russell, S., & Norvig, P. - *Artificial Intelligence: A Modern Approach*, Capítulo 3
- [Pathfinding Algorithms Explained](https://www.redblobgames.com/pathfinding/a-star/introduction.html)
