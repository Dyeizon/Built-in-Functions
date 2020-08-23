# vars([object])
# Retorna o atributo __dict__ de um módulo, classe, instância, ou qualquer outro objeto com um atributo __dict__.
# Sem nenhum argumento,  vars() age como locals().
# Um TypeError é levantado se o objeto especificado não conter um atributo __dict__.


class Vaca:
    """"Esta classe define uma vaca."""
    def mugir(self):
        """Essa função faz com que a instância da vaca muja."""
        som = "Muuuuu!"
        return som


mimosa = Vaca()
print(mimosa.mugir())
print(vars(Vaca))
print(vars(Vaca.mugir))

