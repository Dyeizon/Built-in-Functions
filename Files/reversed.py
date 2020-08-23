# reversed(seq)
# Retorna um iterador reverso.
# seq deve ser um objeto que suporta o protocolo de sequência

listaA = ["Rei", "Rainha", "Valete", "Ás"]
listaB = [1, 2, 3, 4, 5]

for i in reversed(listaA):
    print(i, end=" ")

print()
for i in reversed(listaB):
    print(i, end=" ")