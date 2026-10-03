class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2

# Exemplo
t1 = Triangulo(10, 5)
print("Área:", t1.area())
