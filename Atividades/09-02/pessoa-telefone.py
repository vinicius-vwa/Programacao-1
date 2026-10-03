class Pessoa:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def __str__(self):
        return f"Nome: {self.nome}, Email: {self.email}, Telefone: {self.telefone}"

# Exemplo
joao = Pessoa("João da Silva", "jo@gmail.com", "3237-1234")
print(joao)
