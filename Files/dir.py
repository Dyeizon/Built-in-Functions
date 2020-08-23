# dir([object])
# Sem argumento, retorna a lista de nomes no escopo local
# Com argumento, tenta retornar a lista de atributos válidos para aquele objeto

for i in dir():
    print(i, end="--> ")
    a =  "print(" + i + ")"
    exec(compile(a, "noFile", "exec"))



