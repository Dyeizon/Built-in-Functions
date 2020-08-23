# property(fget=None, fset=None, fdel=None, doc=None)
# Retorna um atributo de propriedade.
# fget é a função para receber um valor de atributo.
# fset é a função para setar um valor de atributo.
# fdel é a função para deletar um valor de atributo.
# doc cria uma docstring para o atributo


class Letra:
    def __init__(self):
        self._x = None

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        print("Deletando a variável <", self._x, ">", sep='')
        del self._x

    x = property(getx, setx, delx, "Diga xiiisss")


A = Letra()
A.x = "Teste"
print(A.x)
del A.x