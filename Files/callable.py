# callable(object)
# Retorna True se o objeto definido como argumento for chamável (callable)

A = "Teste"
B = 12

def func(x):
    return x

print("A -> ", callable(A))
print("B --> ", callable(B))
print("func() --> ", callable(func))
print("print() --> ", callable(print))
