# issubclass(class, classinfo)
# Retorna True se o argumento class for uma subclasse do argumento classinfo.
# Uma classe é considerada uma subclasse de si mesmo.


class Pessoa():
    nome = None
    idade = None


class Predio():
    cor = None
    andares = None
    apartamentos = None

    class Apartamento():
        numero = None
        andar = None
        estaAlugado = None


classes = (Predio, Pessoa)
print(issubclass(Pessoa, Predio))
print(issubclass(Pessoa, Pessoa))

