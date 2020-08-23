# filter(function, iterable)
# Constrói um iterador a partir dos elementos do iterable da qual a function retornar True.
# Se function for None, todos os elementos do iterable que são False são removidos.

listaA = [True, False, False, True, True, True, False]
listaB = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listaC = ("Abacaxi", "Uva", "Melancia", "Pêra", "Maçã")

for i in filter(None, listaA):
    print(i, end=" ")

def par(x):
    if (x % 2 == 0):
        return True
    else:
        return False

print("\nNúmeros pares: ", end="")
for i in filter(par, listaB):
    print(i, end=" ")

def maxLetras(x):
    if (len(x) <=  4):
        return True
    else:
        return False

print("\nFrutas: ", end="")
for i in filter(maxLetras, listaC):
    print(i, end=" ")
        

