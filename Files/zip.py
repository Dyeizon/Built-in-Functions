# zip(*iterables)
# Faz um iterador que agrega os elementos do cada um dos iteráveis dados como argumento.
# Retorna um iterador de tuplas, onde a i° tupla contém o i° elemento de cada um dos argumentos.
# O iterador para quando o menor iterável dado como argumento chega ao fim.

letrasMai = ["A", "B", "C", "D", "E", "F", "G", "H"] # 8 elementos
letrasMin = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]  # 10 elementos

letras = zip(letrasMai, letrasMin)
print(list(letras))  # Foi só até a letra H, pois a lista menor vai até H.
