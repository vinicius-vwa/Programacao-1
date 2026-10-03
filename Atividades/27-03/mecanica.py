# Classe que representa uma pessoa genérica
class Pessoa:
    def __init__(self, nome, telefone, data_nascimento):
        # Atributos básicos de uma pessoa
        self.nome = nome
        self.telefone = telefone
        self.data_nascimento = data_nascimento
    
    def __str__(self):
        # Método especial que define como o objeto será impresso
        return f'''Pessoa:
  Nome: {self.nome}
  Telefone: {self.telefone}
  Data de Nascimento: {self.data_nascimento}
'''


# Classe que representa um cliente (usa uma Pessoa como base)
class Cliente:
    def __init__(self, pessoa, email):
        # Cliente tem uma pessoa associada e um email
        self.pessoa = pessoa
        self.email = email
    
    def __str__(self):
        # Mostra os dados do cliente, acessando os atributos da pessoa
        return f'''Cliente:
  Nome: {self.pessoa.nome}
  Email: {self.email}
  Telefone: {self.pessoa.telefone}
  Data de Nascimento: {self.pessoa.data_nascimento}
'''


# Classe que representa um mecânico (também baseado em Pessoa)
class Mecanico:
    def __init__(self, pessoa):
        self.pessoa = pessoa

    def __str__(self):
        return f'''Mecânico:
  Nome: {self.pessoa.nome}
  Telefone: {self.pessoa.telefone}
  Data de Nascimento: {self.pessoa.data_nascimento}
'''


# Classe que representa um serviço (descrição e valor)
class Servico:
    def __init__(self, descricao, valor):
        self.descricao = descricao
        self.valor = valor

    def __str__(self):
        return f'''Serviço:
  Descrição: {self.descricao}
  Valor: R$ {self.valor}
'''


# Classe que representa um serviço realizado (ligando serviço e mecânico)
class ServicoRealizado:
    def __init__(self, servico, mecanico):
        self.servico = servico
        self.mecanico = mecanico

    def __str__(self):
        return f'''Serviço Realizado:
  Serviço: {self.servico.descricao}
  Valor: R$ {self.servico.valor}
  Mecânico: {self.mecanico.pessoa.nome}
'''


# Classe base para veículos
class Veiculo:
    def __init__(self, placa, cor):
        self.placa = placa
        self.cor = cor

    def __str__(self):
        return f'''Veículo:
  Placa: {self.placa}
  Cor: {self.cor}
'''


# Subclasse de Veiculo para motos
class Moto(Veiculo):
    def __init__(self, placa, cor):
        super().__init__(placa, cor)

    def __str__(self):
        return f'''Moto:
  Placa: {self.placa}
  Cor: {self.cor}
'''


# Subclasse de Veiculo que tem lugares para passageiros
class VeiculoComPassageiros(Veiculo):
    def __init__(self, placa, cor, lugares):
        super().__init__(placa, cor)
        self.lugares = lugares

    def __str__(self):
        return f'''Veículo com Passageiros:
  Placa: {self.placa}
  Cor: {self.cor}
  Lugares: {self.lugares}
'''


# Subclasse de VeiculoComPassageiros para carros
class Carro(VeiculoComPassageiros):
    def __init__(self, placa, cor, lugares, portas):
        super().__init__(placa, cor, lugares)
        self.portas = portas

    def __str__(self):
        return f'''Carro:
  Placa: {self.placa}
  Cor: {self.cor}
  Lugares: {self.lugares}
  Portas: {self.portas}
'''


# Subclasse de VeiculoComPassageiros para ônibus
class Onibus(VeiculoComPassageiros):
    def __init__(self, placa, cor, lugares):
        super().__init__(placa, cor, lugares)

    def __str__(self):
        return f'''Ônibus:
  Placa: {self.placa}
  Cor: {self.cor}
  Lugares: {self.lugares}
'''


# Classe que representa uma ordem de serviço
class OrdemServico:
    def __init__(self, data_entrada, veiculo, data_saida, cliente, desconto, servico_realizado):
        # Ordem de serviço liga cliente, veículo e serviço realizado
        self.data_entrada = data_entrada
        self.veiculo = veiculo
        self.data_saida = data_saida
        self.cliente = cliente
        self.desconto = desconto
        self.servico_realizado = servico_realizado
    
    def __str__(self):
        # Mostra todos os dados da ordem de serviço
        return f'''Ordem de Serviço:
  Data de Entrada: {self.data_entrada}
  Data de Saída: {self.data_saida}
  Desconto: {self.desconto}%
  
{self.cliente}
{self.veiculo}
{self.servico_realizado}
'''
