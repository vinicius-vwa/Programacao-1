class Celular:
    def __init__(self, numero):
        self.numero = numero

class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.celulares = []

    def adicionar_celular(self, celular):
        self.celulares.append(celular)

# Exemplo
p1 = Pessoa("Maria")
p1.adicionar_celular(Celular("47 91234-5678"))
p1.adicionar_celular(Celular("47 98765-4321"))

print(p1.nome, "tem os celulares:")
for c in p1.celulares:
    print("-", c.numero)
