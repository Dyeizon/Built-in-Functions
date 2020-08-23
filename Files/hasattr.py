# hasattr(object, name)
# Retorna True se a String name for um dos atributos do objeto. Caso não seja, retorna falso.

class Carro():
    cor = None
    portas = None

    def buzinar(self):
        print("beep beep")

    def getCor(self):
        return self.cor

    def setCor(self, cor):
        self.cor = cor

    def getPortas(self):
        return self.portas

    def setPortas(self, portas):
        self.portas = portas


car1 = Carro()
car1.setCor("Azul")
print(car1.getCor())
print(hasattr(car1, "buzinar"))
print(hasattr(car1, "cor"))
