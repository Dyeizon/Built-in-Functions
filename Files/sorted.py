# sorted(iterable, *, key=None, reverse=False)
# Retorna uma nova lista sortida dos itens do iterable.
# Tem dois argumentos opcionais que devem ser especificados como keywords.
# key especifica uma função ou um argumento que é usado para extrair uma chave de comparação para cada elemento no iterável
# reverse é um valor boolean. Se True, os elementos da lista são sortidos como se as comparações fossem reversas.

listaA = [5, 1, 2, 77, 9, 553]
# Do menor para o maior
print(sorted(listaA))
# Do maior para o menor
print(sorted(listaA, reverse=True))