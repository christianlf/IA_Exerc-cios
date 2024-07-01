import numpy as np
class VetorOrdenado:
  
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    def imprime(self):
        if self.ultima_posicao == -1:
            print('O vetor está vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, ' - ', self.valores[i])

    def insere(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade máxima atingida')
            return

        posicao = 0
        for i in range(self.ultima_posicao + 1):
            posicao = i
            if self.valores[i] > valor:
                break
            if i == self.ultima_posicao:
                posicao = i + 1

        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x + 1] = self.valores[x]
            x -= 1

        self.valores[posicao] = valor
        self.ultima_posicao += 1

# Função principal
def main():
    capacidade = int(input("Digite a capacidade do vetor: "))
    vetor = VetorOrdenado(capacidade)

    while True:
        valor = int(input("Digite um valor para inserir no vetor (ou -1 para sair): "))
        if valor == -1:
            break
        vetor.insere(valor)
        print("Vetor após inserção:")
        vetor.imprime()

if __name__ == "__main__":
    main()
