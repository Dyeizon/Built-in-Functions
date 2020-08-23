# compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)
# Compila a source em um código ou objeto AST (Abstract Syntax Tree)
# O argumento filename deve referenciar o arquivo do qual o código foi lido.
# Caso não tenha sido de um arquivo, utilize '<string>'
# O argumento mode especifica qual tipo de código deve ser compilado,
# pode ser:
# 'exec' -> se a source consiste em uma sequência de afirmações.
# 'eval' -> se a source consiste em uma única expressão.
# 'single' -> se a source consiste em uma única afirmação interativa.

print("Compilar um código em forma de texto em uma variável")
codeInVar = 'A = str(input("Digite seu nome: "))\nprint("Bem vindo,", A)'
exec(compile(codeInVar, 'noFilename', 'exec'))
