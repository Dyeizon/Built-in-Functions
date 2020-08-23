# frozenset([iterable])
# Retorna um objeto frozenset, opcionalmente com os elementos recebidos do iterável.
# frozenset é uma classe similar ao set(), mas seus dados são imutáveis.

frSet = frozenset("12345")
print(frSet)
# Uma string é um objeto iterável

normalSet = (1,2,3,4,5,5,5,5,5)
print(normalSet)
print(frozenset(normalSet))
