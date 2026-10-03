class Pessoa:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def __str__(self):   # <-- precisa estar dentro da classe
        return f"Nome = {self.nome}, Email = {self.email}, Telefone = {self.telefone}"

# Criando objetos
joao = Pessoa("João", "joao@gmail.com", "01 12345678")
maria = Pessoa("Maria", "maria@gmail.com", "02 87654321")

# Guardando em uma lista
pessoas = [joao, maria]

# Percorrendo a lista
for p in pessoas:
    print(p)
