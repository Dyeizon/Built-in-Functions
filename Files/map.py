# map(function, iterable, ...)
# Retorna um iterador que aplica a function para cada item do iterable, produzindo os resultados.

sons = ("beep beep", "bip bop", "bi bi")


def buzinar(som):
    return som


A = map(buzinar, sons)
print(list(A))