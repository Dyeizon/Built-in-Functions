# divmod(a, b)
# Recebe dois números não-complexos como argumentos, e retorna um par de números
# consistindo em seu quociente e resto quando utilizando divisão inteira.

numA = float(input("Digite um número A: "))
numB = float(input("Digite um número B: "))

varA = divmod(numA, numB)

print("Quociente:", varA[0])
print("Resto:", varA[1])


