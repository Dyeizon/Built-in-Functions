# @staticmethod
# Transforma um método em um método estático
# Um método estático não recebe um argumento primário explícito.


class Vaca:
    @staticmethod
    def sound(times):
        for i in range(times):
            print("MUUUU!")

mimosa = Vaca()
mimosa.sound(10)