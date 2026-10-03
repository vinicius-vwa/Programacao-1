class Pessoa:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def __str__(self):
        return f"Nome = {self.nome}, Email = {self.email}, Telefone = {self.telefone}"

joao = Pessoa("João", "joãozinho@gmail.com", "3478643782")
print(joao)

maria = Pessoa("Maria", "mariazinha@gmail.com", "347902584578")
print(maria)

jose = Pessoa("José", "zezinho@gmail.com", "6905787568")
print(jose)