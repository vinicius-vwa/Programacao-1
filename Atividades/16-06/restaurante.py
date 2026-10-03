from datetime import date
from typing import List

class Cliente:
    def __init__ (self, nome:str, data_nascimento: date, cpf:str):
        self.nome: str = nome
        self.data_nascimento: date = data_nascimento
        self.cpf: str = cpf

class Prato:
    def __init__(self, nome: str, ingredientes: List[str], modo_preparo: str, preco: float):
        self.nome: str = nome
        self.ingredientes: List[str] = ingredientes
        self.modo_preparo: str = modo_preparo
        self.preco: float = preco

class Pedido:
    def __init__ (self, data_pedido: date, percentual_desconto: float, valor_final: float, cliente: Cliente, pratos: list[Prato]):
        self.data_pedido: date = data_pedido
        self.percentual_desconto: float = percentual_desconto
        self.valor_final: float = valor_final
        self.cliente: Cliente = cliente
        self.pratos: List[Prato] = pratos


cliente1 = Cliente(
    nome="João Silva", 
    data_nascimento=date(1995, 5, 20), 
    cpf="123.456.789-00"
)

prato1 = Prato(
    nome="Lasanha", 
    ingredientes=["Massa", "Molho à Bolonhesa", "Queijo"], 
    modo_preparo="Montar as camadas e levar ao forno por 30 minutos.", 
    preco=45.0
)

prato2 = Prato(
    nome="Suco de Laranja", 
    ingredientes=["Laranjas", "Gelo"], 
    modo_preparo="Espremer as laranjas e misturar com gelo.", 
    preco=8.0
)

novo_pedido = Pedido(
    data_pedido=date.today(),
    percentual_desconto=10.0,
    valor_final=47.7, # (45 + 8) com 10% de desconto
    cliente=cliente1,
    pratos=[prato1, prato2]
)

print(f"Pedido feito por: {novo_pedido.cliente.nome}")
print("Itens do pedido:")
for prato in novo_pedido.pratos:
    print(f"- {prato.nome}: R$ {prato.preco:.2f}")
print(f"Valor Total a pagar: R$ {novo_pedido.valor_final:.2f}")