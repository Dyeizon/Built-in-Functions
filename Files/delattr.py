# delattr(object, name)
# Essa função é relativa à setattr().
# Os argumentos são um objeto e uma String.
# A String deve ser o nome de um dos atributos do objeto.
# Essa função deleta o atributo nomeado do objeto.

class Cadeira:
    material = "Madeira"
    pernas = 4
    altura = 120

delattr(Cadeira, "pernas")
print(Cadeira().material)
# print(Cadeira().pernas) ESTE COMANDO DARÁ ERRO, POIS O ATRIBUTO FOI DELETADO
print(Cadeira().altura)
