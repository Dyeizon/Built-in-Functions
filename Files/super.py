# super([type[, object-or-type]])
# Faz referência à super classe de uma sub classe.


class Pai:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        print("Construindo a classe Pai")


class Filha(Pai):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        print("Construindo a classe Filha")


f1 = Filha("Magda", 18)