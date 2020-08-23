# hash(object)
# Retorna o valor hash do objeto (se tiver).
# Valores hash são inteiros, eles são usados para comparar rapidamente keys de dicionários.

eu = {
    "nome" : "Dyeizon",
    "idade" : 17,
    "altura" : "bastante"
}

print(hash(eu["nome"]))
print(hash("String"))