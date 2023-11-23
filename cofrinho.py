from enum import Enum

class Moeda(Enum):
    dez = 10
    vinte_cinco = 25
    cinquenta = 50
    cem = 100

class Item:
    def __init__(self, descricao, volume):
        self.descricao = descricao
        self.volume = volume

class Cofrinho:
    def __init__(self, cor, volume_Max):
        self.cor = cor
        self.volume_Max = volume_Max
        self.volume_atual = 0
        self.moedas = []
        self.itens = []

    def volume_disponivel(self):
        return self.volume_maximo - self.volume_atual

    def adicionar_moeda(self, moeda):
        if self.volume_disponivel() >= moeda.value:
            self.moedas.append(moeda)
            self.volume_atual += moeda.value
            print(f"Moeda de {moeda.value} inserida no cofre.")
        else:
            print("Volume insuficiente para a moeda.")

    def adicionar_item(self, item):
        if self.volume_disponivel() >= item.volume:
            self.itens.append(item)
            self.volume_atual += item.volume
            print(f"Item '{item.descricao}' inserido no cofre.")
        else:
            print("Volume insuficiente para o item.")

    def quebrar_cofre(self):
        print(f"Cofre quebrado!")
        self.moedas = []
        self.itens = []
        self.volume_atual = 0

    def olhar_conteudo(self):
        print(f"\nConteúdo do cofre:")
        print(f"Moedas: {[moeda.value for moeda in self.moedas]}")
        print(f"Itens: {[item.descricao for item in self.itens]}")

    def valor_total(self):
        valor_moedas = sum([moeda.value for moeda in self.moedas])
        print(f"Valor total em moedas no cofre: {valor_moedas}")
