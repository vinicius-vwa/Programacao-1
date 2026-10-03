from datetime import date

class Pessoa:
    def __init__(self, nome: str, email: str):
        self.nome = nome
        self.email = email

class Livro:
    def __init__(self, nome: str, autor: str, dono: Pessoa):
        self.nome = nome
        self.autor = autor
        self.dono = dono

class Emprestimo:
    def __init__(self, livro: Livro, pessoa: Pessoa, data_pegou: date):
        self.livro = livro
        self.pessoa = pessoa
        self.data_pegou = data_pegou


# Criando pessoas
p1 = Pessoa("João da Silva", "josilva@gmail.com")
p2 = Pessoa("Maria Oliveira", "maliv@gmail.com")
p3 = Pessoa("Tiago Lemes", "tile@gmail.com")

# Livros de João
liv1 = Livro("O Senhor do Anéis: A sociedade do Anel", "John Ronald Reuel Tolkien", p1)
liv2 = Livro("As batalhas do castelo", "Domingos Pellegrini", p1)

# Livros de Maria
liv3 = Livro("Prisioneiros na biblioteca", "Manuel Filho", p2)
liv4 = Livro("A Guardiã de pedras", "Cristina Bomfim", p2)

# Empréstimos
emprestimos = []
e1 = Emprestimo(liv3, p3, date(2026, 2, 10))
emprestimos.append(e1)

# Processamento: mostrar quais livros estão emprestados
print("LIVROS EMPRESTADOS")
for emp in emprestimos:
    print(f"Livro: {emp.livro.nome}")
    print(f"Autor: {emp.livro.autor}")
    print(f"Dono: {emp.livro.dono.nome}")
    print(f"Emprestado para: {emp.pessoa.nome}")
    print(f"Data do empréstimo: {emp.data_pegou}")
    print("--------------------------")
