class Vertice:

  def __init__(self, rotulo, distancia_objetivo):
    self.rotulo = rotulo
    self.visitado = False
    self.distancia_objetivo = distancia_objetivo
    self.adjacentes = []

  def adiciona_adjacente(self, adjacente):
    self.adjacentes.append(adjacente)

  def mostra_adjacentes(self):
    for i in self.adjacentes:
      print(i.vertice.rotulo, i.custo)
class Adjacente:
  def __init__(self, vertice, custo):
    self.vertice = vertice
    self.custo = custo

    # Novo atributo
    self.distancia_aestrela = vertice.distancia_objetivo + self.custo
class Grafo:
  Porto_uniao = Vertice('Porto_uniao', 203)
  Paulo_Frontin = Vertice('Paulo_Frontin', 172)
  Canoinhas = Vertice('Canoinhas', 141)
  tres_barras = Vertice('tres_barras', 131)
  Sao_mateus = Vertice('Sao_mateus', 123)
  Irati = Vertice('Irati', 139)
  Curitiba = Vertice('Curitiba', 0)
  Palmeira = Vertice('Palmeira', 59)
  Mafra = Vertice('Mafra', 94)
  Campo_largo = Vertice('Campo_largo', 27)
  Balsa_Nova = Vertice('Balsa_Nova', 41)
  Lapa = Vertice('Lapa', 74)
  tijuca_sul = Vertice('tijuca_sul', 56)
  Araucara = Vertice('Araucara', 23)
  Sao_jose_dos_pinhais = Vertice('Sao_jose_dos_pinhais', 13)
  Contenda = Vertice('Contenda', 39)

  Porto_uniao.adiciona_adjacente(Adjacente(Paulo_Frontin, 46))
  Porto_uniao.adiciona_adjacente(Adjacente(Sao_mateus, 87))
  Porto_uniao.adiciona_adjacente(Adjacente(Canoinhas, 78))

  Paulo_Frontin.adiciona_adjacente(Adjacente(Porto_uniao, 46))
  Paulo_Frontin.adiciona_adjacente(Adjacente(Irati, 75))

  Sao_mateus.adiciona_adjacente(Adjacente(Irati, 57))
  Sao_mateus.adiciona_adjacente(Adjacente(Porto_uniao, 87))
  Sao_mateus.adiciona_adjacente(Adjacente(tres_barras, 43))
  Sao_mateus.adiciona_adjacente(Adjacente(Lapa, 60))
  Sao_mateus.adiciona_adjacente(Adjacente(Palmeira, 77))
 

  Irati.adiciona_adjacente(Adjacente(Sao_mateus, 57))
  Irati.adiciona_adjacente(Adjacente(Paulo_Frontin, 75))
  Irati.adiciona_adjacente(Adjacente(Palmeira, 75))

  Canoinhas.adiciona_adjacente(Adjacente(Porto_uniao, 78))
  Canoinhas.adiciona_adjacente(Adjacente(tres_barras, 12))

  tres_barras.adiciona_adjacente(Adjacente(Sao_mateus, 78))
  tres_barras.adiciona_adjacente(Adjacente(Canoinhas, 12))

  Palmeira.adiciona_adjacente(Adjacente(Irati, 75))
  Palmeira.adiciona_adjacente(Adjacente(Sao_mateus, 77))
  Palmeira.adiciona_adjacente(Adjacente(Campo_largo, 55))

  Lapa.adiciona_adjacente(Adjacente(Sao_mateus, 60))
  Lapa.adiciona_adjacente(Adjacente(Mafra, 57))
  Lapa.adiciona_adjacente(Adjacente(Contenda, 26))

  Mafra.adiciona_adjacente(Adjacente(Lapa, 57))
  Mafra.adiciona_adjacente(Adjacente(Canoinhas, 66))
  Mafra.adiciona_adjacente(Adjacente(tijuca_sul, 99))

  Contenda.adiciona_adjacente(Adjacente(Lapa, 26))
  Contenda.adiciona_adjacente(Adjacente(Araucara, 18))
  Contenda.adiciona_adjacente(Adjacente(Balsa_Nova, 19))

  Balsa_Nova.adiciona_adjacente(Adjacente(Curitiba, 51))
  Balsa_Nova.adiciona_adjacente(Adjacente(Campo_largo, 22))
  Balsa_Nova.adiciona_adjacente(Adjacente(Contenda, 19))


  Araucara.adiciona_adjacente(Adjacente(Contenda, 18))
  Araucara.adiciona_adjacente(Adjacente(Curitiba, 37))

  tijuca_sul.adiciona_adjacente(Adjacente(Mafra, 99))
  tijuca_sul.adiciona_adjacente(Adjacente(Sao_jose_dos_pinhais, 49))
  
  Campo_largo.adiciona_adjacente(Adjacente(Palmeira, 55))
  Campo_largo.adiciona_adjacente(Adjacente(Balsa_Nova, 22))
  Campo_largo.adiciona_adjacente(Adjacente(Curitiba, 29))
  
  Sao_jose_dos_pinhais.adiciona_adjacente(Adjacente(tijuca_sul, 49))
  Sao_jose_dos_pinhais.adiciona_adjacente(Adjacente(Curitiba, 15))
  
  Curitiba.adiciona_adjacente(Adjacente(Campo_largo, 29))
  Curitiba.adiciona_adjacente(Adjacente(Balsa_Nova, 51))
  Curitiba.adiciona_adjacente(Adjacente(Araucara, 37))
  Curitiba.adiciona_adjacente(Adjacente(Sao_jose_dos_pinhais, 15))
  
import numpy as np
class VetorOrdenado:
  
  def __init__(self, capacidade):
    self.capacidade = capacidade
    self.ultima_posicao = -1
    # Mudança no tipo de dados
    self.valores = np.empty(self.capacidade, dtype=object)

  # Referência para o vértice e comparação com a distância para o objetivo
  def insere(self, adjacente):
    if self.ultima_posicao == self.capacidade - 1:
      print('Capacidade máxima atingida')
      return
    posicao = 0
    for i in range(self.ultima_posicao + 1):
      posicao = i
      if self.valores[i].distancia_aestrela > adjacente.distancia_aestrela:
        break
      if i == self.ultima_posicao:
        posicao = i + 1
    x = self.ultima_posicao
    while x >= posicao:
      self.valores[x + 1] = self.valores[x]
      x -= 1
    self.valores[posicao] = adjacente
    self.ultima_posicao += 1

  def imprime(self):
    if self.ultima_posicao == -1:
      print('O vetor está vazio')
    else:
      for i in range(self.ultima_posicao + 1):
        print(i, ' - ', self.valores[i].vertice.rotulo, ' - ', 
              self.valores[i].custo, ' - ', 
              self.valores[i].vertice.distancia_objetivo, ' - ',
              self.valores[i].distancia_aestrela)  
class AEstrela:
  def __init__(self, objetivo):
    self.objetivo = objetivo
    self.encontrado = False

  def buscar(self, atual):
    print('------------------')
    print('Atual: {}'.format(atual.rotulo))
    atual.visitado = True

    if atual == self.objetivo:
      self.encontrado = True
    else:
      vetor_ordenado = VetorOrdenado(len(atual.adjacentes))
      for adjacente in atual.adjacentes:
        if adjacente.vertice.visitado == False:
          adjacente.vertice.visitado = True
          vetor_ordenado.insere(adjacente)
      vetor_ordenado.imprime()

      if vetor_ordenado.valores[0] != None:
        self.buscar(vetor_ordenado.valores[0].vertice)
# Função para solicitar os vértices inicial e objetivo ao usuário
def solicitar_vertices():
    vertice_inicial = input("Digite o vértice inicial: ").capitalize()
    vertice_objetivo = input("Digite o vértice objetivo: ").capitalize()
    return vertice_inicial, vertice_objetivo

# Solicita os vértices inicial e objetivo ao usuário
vertices = solicitar_vertices()

# Função principal que coordena a execução da busca
def main():
    vertice_inicial, vertice_objetivo = vertices
    # Encontra o vértice inicial no grafo
    if hasattr(Grafo, vertice_inicial.capitalize()):
        inicio = getattr(Grafo, vertice_inicial.capitalize())
    else:
        print("Vértice inicial não encontrado no grafo.")
        return

    # Encontra o vértice objetivo no grafo
    if hasattr(Grafo, vertice_objetivo.capitalize()):
        objetivo = getattr(Grafo, vertice_objetivo.capitalize())
    else:
        print("Vértice objetivo não encontrado no grafo.")
        return

    # Inicia a busca gulosa
    busca = AEstrela(objetivo)
    busca.buscar(inicio)

# Executa a função principal
if __name__ == "__main__":
    main()


