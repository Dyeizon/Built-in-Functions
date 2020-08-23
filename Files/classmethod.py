# @classmethod ou classmethod(method)
# Transforma um método em um método de classe
# Utilize @classmethod antes de criar o método.

class A:
    def function(cls):
        print("Funcionando perfeitamente.")
    classmethod(function)

A().function()
