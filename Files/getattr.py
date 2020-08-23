# getattr(object, name[, default])
# Retorna o valor do atributo nomeado de objeto.
# name deve ser uma String.
# Se a String name for um dos atributos do objeto, o resultado é o valor do atributo.


class Pessoa():
    nome = None
    idade = None
    cpf = None


p1 = Pessoa()
p1.nome = "Pedro"
print(getattr(p1, "nome"))
print(p1.nome)
