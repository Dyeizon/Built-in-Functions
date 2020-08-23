# iter(object[, sentinel])
# Retorna um objeto iterador.
# O primeiro argumento é interpretado diferentemente dependendo da presença do segundo argumento.
# Sem o segundo argumento, object deve ser uma coleção que suporta iteração.
# Se o segundo argumento for setado, o objeto deve ser invocável (callable).

A = iter("Teste")
for i in A:
    print(i)


class Pessoa():
    nome = "Maria"


B = iter(Pessoa, 1)
print(B)