# next(iterator[, default])
# Retorna o próximo item do iterator chamando o método __next__().
# Se o argumento default for dado, ele é retornado se o iterador se exaurir.

listaA = iter(["Azul", "Branco", "Roxo", "Rosa", "Verde"])
for i in range(0, 10):
    print(next(listaA, "Acabaram as cores!"))