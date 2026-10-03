class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

# Exemplo
r1 = Retangulo(4, 6)
print("Área:", r1.area())
