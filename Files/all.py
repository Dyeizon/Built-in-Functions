# all()
# Retorna True se todos os elementos do iterável são True
# (ou se o iterável estiver vazio)
# Equivalente a:
#def all(iterable):
#    for element in iterable:
#        if not element:
#            return False
#    return True

listaA = [True, False, True, True]
listaB = [True, True, True, True]
listaC = []
listaD = ["Peixe", "Macaco", "Gato", "Cachorro"]

print("Lista A: ")
print(listaA)
print("all(): ", all(listaA))

print("\nLista B: ")
print(listaB)
print("all(): ", all(listaB))

print("\nLista C: ")
print(listaC)
print("all(): ", all(listaC))

print("\nLista D: ")
print(listaD)
print("all(): ", all(listaD))


