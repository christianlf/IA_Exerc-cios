import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Criação das variáveis de entrada
qualidade = ctrl.Antecedent(np.arange(0, 11, 1), 'qualidade')
servico = ctrl.Antecedent(np.arange(0, 11, 1), 'servico')

# Criação da variável de saída
gorjeta = ctrl.Consequent(np.arange(0, 21, 1), 'gorjeta')

# Definição das funções de pertinência para as entradas
qualidade.automf(number=3, names=['ruim', 'boa', 'saborosa'])
servico.automf(number=3, names=['ruim', 'aceitavel', 'excelente'])

# Definição das funções de pertinência para a saída (gorjeta)
gorjeta['baixa'] = fuzz.sigmf(gorjeta.universe, 5, -1)
gorjeta['media'] = fuzz.gaussmf(gorjeta.universe, 10,1)
gorjeta['alta'] = fuzz.pimf(gorjeta.universe,10, 20, 20,21)

# Regras fuzzy
rule1 = ctrl.Rule(qualidade['ruim'] | servico['ruim'], gorjeta['baixa'])
rule2 = ctrl.Rule(servico['aceitavel'], gorjeta['media'])
rule3 = ctrl.Rule(servico['excelente'] & qualidade['saborosa'], gorjeta['alta'])  # Operação 'and' entre excelência e saborosa

# Controle do sistema
gorjeta_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
gorjeta_simulacao = ctrl.ControlSystemSimulation(gorjeta_ctrl)

# Inserção dos valores de entrada
qualidade_input = 10
servico_input = 10

gorjeta_simulacao.input['qualidade'] = qualidade_input
gorjeta_simulacao.input['servico'] = servico_input

# Computar a saída
gorjeta_simulacao.compute()

# Resultado da gorjeta do sistema fuzzy
resultado_gorjeta = gorjeta_simulacao.output['gorjeta']
print(f"Gorjeta do sistema fuzzy: {resultado_gorjeta}")

# Exibição do gráfico da variável de saída gorjeta após a simulação
gorjeta.view(sim=gorjeta_simulacao)
plt.show()
