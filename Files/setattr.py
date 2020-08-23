# setattr(object, name, value)
# name deve nomear um atributo existente ou um novo atributo.
# A função atribui o valor ao atributo.
# setattr(ObjetoQualquer, 'atributo', 10) == ObjetoQualquer.atributo = 10


class C:
    def __init__(self, nome):
        self._nome = nome

    padrao = 10

    def getnome(self):
        print("Seu nome é " + str(self._nome))


p1 = C("Luiz")
setattr(p1, "padrao", 11)
p1.getnome()
print(p1.padrao)






