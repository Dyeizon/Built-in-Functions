# isinstance(object, classinfo)
# Retorna True se o argumento object for uma instância do argumento classinfo. Caso não seja, retorna False.

class Pessoa():
    nome = None
    idade = None


class Predio():
    cor = None
    andares = None
    apartamentos = None


predio1 = Predio()
predio2 = None
predio1.cor = "Roxo"
classes = (Predio, Pessoa)
print(isinstance(predio1, Predio))
print(isinstance(predio2, Predio))
print(isinstance(predio1, classes))
