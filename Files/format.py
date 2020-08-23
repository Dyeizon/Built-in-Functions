# format(value[, format_spec])
# Converte um value em uma representação formatada, controlada por format_spec.

nome = str(input("Nome: "))
idade = int(input("Idade: "))
peso = float(input("Peso: "))
print("Olá {0}, você tem {1} anos e seu peso é de {2:.1f}kg aproximadamente.".format(nome, idade, peso))
