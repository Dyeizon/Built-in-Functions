# slice(stop)
# slice(start, stop[, step])
# Retorna um objeto slice representando o set de índices especificado por range(start, stop, step).
# O argumento start por padrão é None.

# Começa no índice 1, vai até o 12, pulando de 2 em 2
fatiador = slice(1, 12, 2)
texto = "Eu gosto muito de passear"
print(texto[fatiador])