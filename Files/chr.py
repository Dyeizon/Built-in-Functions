# chr(i)
# Retorna uma String representando o valor Unicode de um inteiro i.
from time import sleep

numeros = []
letrasUp = []
letrasLow = []

for i in range(48, 57+1):
    numeros.append(int(chr(i)))
print("Números: ", numeros)

for i in range(65, 90+1):
    letrasUp.append(chr(i))
print("Letras maiúsculas: ", letrasUp)

for i in range(97, 122+1):
    letrasLow.append(chr(i))
print("Letras minúsculas: ", letrasLow)




