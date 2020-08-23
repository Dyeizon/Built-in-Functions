# enumerate(iterable, start=0)
# Retorna um objeto enumerável.
# O argumento iterable deve ser uma sequência, um iterador ou outro objeto que suporte iteração.
# O argumento start (por padrão 0) define o início da contagem.

listaA = ["Abacaxi", "Limão", "Uva", "Melancia", "Maçã", "Goiaba"]

print("Lista de compras: ")
for indice, valor in enumerate(listaA, 1):
    print(indice,": ",valor)
