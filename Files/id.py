# id(object)
# Retorna a "identidade" de um objeto.
# id é um número inteiro único e constante para o objeto durante sua existência.
# Dois objetos não devem ter o mesmo id.


class Pessoa():
    nome = None
    idade = int

    def aniversario(self):
        self.idade = self.idade + 1


print(id(Pessoa))
p1 = Pessoa()
print(id(p1))
p1.idade = 17
p1.aniversario()
print(p1.idade)
