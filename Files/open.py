# open(file, mode='r', buffering=-1, encoding==None, errors=None, newLine=None, closefd=True, opener=None)
# Abre o file e retorna um objeto file correspondente.
# Se o arquivo não pode ser aberto, o erro OSError é levantado.
# file é um objeto de caminho, é preciso dar o diretório do arquivo (absoluto ou relativo ao diretório atual)
# mode é uma String opcional que especifica o modo o qual o arquivo será aberto.
# 'r' = leitura apenas
# 'w' = escrita apenas
# 'x' = criação exclusiva
# 'a' = acréscimo
# 'b' = modo binário
# 't' = modo texto
# '+' = atualização (leitura e escrita)

A = open("open.txt", 'w')
for i in range(0, 101):
    A.write(str(i)+"\n")

A.close()
