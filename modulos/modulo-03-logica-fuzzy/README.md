# 🎛️ Módulo 3: Lógica Fuzzy

## Descrição

Implementações de sistemas de lógica difusa (Fuzzy Logic) usando **Scikit-Fuzzy**, explorando conjuntos fuzzy, regras de inferência e aplicações práticas.

## Arquivos

### `skfuzzy.py`
**Biblioteca:** Scikit-Fuzzy

**Descrição:**
- Implementação de sistemas de lógica fuzzy
- Conjuntos fuzzy e funções de pertinência
- Sistemas de inferência fuzzy (FIS)
- Defuzzificação

## Conceitos Teóricos

### O que é Lógica Fuzzy?

**Lógica Clássica (Booleana):**
- Valores binários: 0 ou 1, Verdadeiro ou Falso
- Exemplo: "É jovem?" → Sim (1) ou Não (0)

**Lógica Fuzzy:**
- Valores contínuos entre 0 e 1
- Graus de pertinência parcial
- Exemplo: "É jovem?" → 0.7 (70% jovem)

### Por que usar Lógica Fuzzy?

✅ **Modelagem de incerteza** humana  
✅ **Controle suave** sem transições abruptas  
✅ **Linguagem natural** em regras  
✅ **Sistemas não-lineares** complexos  

### Componentes de um Sistema Fuzzy

#### 1. Fuzzificação
Conversão de valores numéricos em graus de pertinência fuzzy.

**Exemplo:**
```
Temperatura = 25°C
→ Frio: 0.0
→ Morno: 0.7
→ Quente: 0.3
```

#### 2. Conjuntos Fuzzy
Definição de categorias com funções de pertinência.

**Tipos de funções:**
- **Triangular:** `trimf(x, [a, b, c])`
- **Trapezoidal:** `trapmf(x, [a, b, c, d])`
- **Gaussiana:** `gaussmf(x, mean, sigma)`
- **Sigmoidal:** `sigmf(x, b, c)`

#### 3. Regras Fuzzy
Inferência baseada em regras IF-THEN.

**Exemplo:**
```
SE temperatura é FRIA E umidade é ALTA
ENTÃO ventilador é LENTO

SE temperatura é QUENTE E umidade é BAIXA
ENTÃO ventilador é RÁPIDO
```

#### 4. Defuzzificação
Conversão do resultado fuzzy em valor numérico.

**Métodos:**
- **Centróide:** Centro de área
- **Bissetor:** Divide área ao meio
- **MOM:** Mean of Maximum
- **SOM/LOM:** Smallest/Largest of Maximum

## Como Executar

```bash
# Instalar dependências
pip install scikit-fuzzy numpy matplotlib

# Executar implementação
python skfuzzy.py
```

## Exemplo de Uso

### Sistema de Controle de Gorjeta

```python
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# 1. Definir variáveis de entrada e saída
qualidade = ctrl.Antecedent(np.arange(0, 11, 1), 'qualidade')
servico = ctrl.Antecedent(np.arange(0, 11, 1), 'servico')
gorjeta = ctrl.Consequent(np.arange(0, 26, 1), 'gorjeta')

# 2. Criar funções de pertinência
qualidade['ruim'] = fuzz.trimf(qualidade.universe, [0, 0, 5])
qualidade['boa'] = fuzz.trimf(qualidade.universe, [0, 5, 10])
qualidade['ótima'] = fuzz.trimf(qualidade.universe, [5, 10, 10])

servico['ruim'] = fuzz.trimf(servico.universe, [0, 0, 5])
servico['bom'] = fuzz.trimf(servico.universe, [0, 5, 10])
servico['ótimo'] = fuzz.trimf(servico.universe, [5, 10, 10])

gorjeta['baixa'] = fuzz.trimf(gorjeta.universe, [0, 0, 13])
gorjeta['média'] = fuzz.trimf(gorjeta.universe, [0, 13, 25])
gorjeta['alta'] = fuzz.trimf(gorjeta.universe, [13, 25, 25])

# 3. Definir regras
regra1 = ctrl.Rule(qualidade['ruim'] | servico['ruim'], gorjeta['baixa'])
regra2 = ctrl.Rule(servico['bom'], gorjeta['média'])
regra3 = ctrl.Rule(servico['ótimo'] | qualidade['ótima'], gorjeta['alta'])

# 4. Criar sistema de controle
sistema_gorjeta = ctrl.ControlSystem([regra1, regra2, regra3])
gorjeta_calculada = ctrl.ControlSystemSimulation(sistema_gorjeta)

# 5. Fornecer entradas
gorjeta_calculada.input['qualidade'] = 6.5
gorjeta_calculada.input['servico'] = 9.8

# 6. Computar resultado
gorjeta_calculada.compute()
print(f"Gorjeta: {gorjeta_calculada.output['gorjeta']:.2f}%")
```

### Visualização de Conjuntos Fuzzy

```python
import matplotlib.pyplot as plt

# Visualizar funções de pertinência
qualidade.view()
servico.view()
gorjeta.view()
plt.show()
```

## Aplicações Práticas

### 1. Controle de Ar-Condicionado
**Entradas:** Temperatura, Umidade  
**Saída:** Velocidade do ventilador

### 2. Sistema de Freio ABS
**Entradas:** Velocidade, Pressão no pedal  
**Saída:** Força de frenagem

### 3. Câmera Autofocus
**Entradas:** Distância, Luz ambiente  
**Saída:** Posição da lente

### 4. Lavadora de Roupas
**Entradas:** Sujeira, Quantidade de roupa  
**Saída:** Tempo de lavagem, Quantidade de sabão

### 5. Diagnóstico Médico
**Entradas:** Sintomas (febre, dor, etc.)  
**Saída:** Probabilidade de doença

## Operadores Fuzzy

### Operações em Conjuntos Fuzzy

**União (OR):**
```python
resultado = fuzz.fuzzy_or(A, B)  # max(A, B)
```

**Interseção (AND):**
```python
resultado = fuzz.fuzzy_and(A, B)  # min(A, B)
```

**Complemento (NOT):**
```python
resultado = fuzz.fuzzy_not(A)  # 1 - A
```

## Vantagens e Desvantagens

### ✅ Vantagens
- Modela conhecimento humano impreciso
- Controle suave sem descontinuidades
- Fácil compreensão (regras em linguagem natural)
- Robusto a ruídos e incertezas
- Não requer modelo matemático preciso

### ⚠️ Desvantagens
- Ajuste manual de parâmetros
- Difícil validação formal
- Pode ser complexo com muitas variáveis
- Nem sempre é a melhor solução (alternativas: redes neurais, ML)

## Comparação: Lógica Fuzzy vs. Machine Learning

| Aspecto | Lógica Fuzzy | Machine Learning |
|---------|--------------|------------------|
| **Conhecimento** | Especialista define regras | Aprende dos dados |
| **Interpretabilidade** | Alta (regras claras) | Baixa (caixa-preta) |
| **Dados necessários** | Poucos | Muitos |
| **Adaptação** | Manual | Automática |
| **Melhor para** | Controle, sistemas especialistas | Classificação, previsão |

## Exercícios Sugeridos

1. **Sistema de Controle de Velocidade:** Cruise control de veículo
2. **Avaliação de Risco:** Sistema de crédito bancário
3. **Controle de Iluminação:** Ajuste automático de brilho
4. **Sistema de Irrigação:** Controle baseado em umidade do solo

## Referências

- [Scikit-Fuzzy Documentation](https://pythonhosted.org/scikit-fuzzy/)
- Zadeh, L. A. - *Fuzzy Sets* (1965)
- Mamdani, E. H. - *Application of Fuzzy Algorithms for Control of Simple Dynamic Plant*
- [Fuzzy Logic Tutorial](https://www.geeksforgeeks.org/fuzzy-logic-introduction/)

## Recursos Adicionais

- [Interactive Fuzzy Logic Tool](https://www.mathworks.com/products/fuzzy-logic.html)
- [Fuzzy Logic in Python - Real Python](https://realpython.com/)
- Video: [Introduction to Fuzzy Logic](https://www.youtube.com/watch?v=__0nZuG4sTw)
