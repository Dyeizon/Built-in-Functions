# memoryview(object)
# Retorna um objeto "memory view" criado a partir do argumento dado.

byteArray = bytearray('ABC', 'utf-8')
mv = memoryview(byteArray)
print("Valores ASCII")
print(mv[0])
print(mv[1])
print(mv[2])
print(bytes(mv[0:2]))