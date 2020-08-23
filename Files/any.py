# any(iterable)
# Retorna True se qualquer elemento do iterável for True.
# Se o iterável estiver vazio, retorna False.
# Equivalente a:
# def any(iterable):
#    for element in iterable:
#        if element:
#            return True
#    return False

listaA = [True, False, True, True]
listaB = [True, True, True, True]
listaC = []
listaD = ["Peixe", "Macaco", "Gato", "Cachorro"]

print("Lista A: ")
print(listaA)
print("any(): ", any(listaA))

print("\nLista B: ")
print(listaB)
print("any(): ", any(listaB))

print("\nLista C: ")
print(listaC)
print("any(): ", any(listaC))

print("\nLista D: ")
print(listaD)
print("any(): ", any(listaD))
