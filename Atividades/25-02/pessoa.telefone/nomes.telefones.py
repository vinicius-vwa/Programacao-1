# Importa o módulo de testes do Python
import unittest
# Importa a classe date para trabalhar com datas
from datetime import date
# Importa todas as classes do arquivo mecanica.py
from mecanica import *

# Classe de testes que herda de unittest.TestCase
class TestarSistema(unittest.TestCase):
    
    # Método de teste: verifica se a criação dos objetos funciona corretamente
    def test_criacao(self):
        # Cria uma pessoa
        pessoa = Pessoa("João da Silva", "47 9 1234 5678", date(1976, 1, 1))
        # Cria um cliente a partir da pessoa
        cliente = Cliente(pessoa, "josilva@gmail.com")

        # Verifica se os atributos do cliente estão corretos
        self.assertEqual(cliente.pessoa.nome, "João da Silva")
        self.assertEqual(cliente.email, "josilva@gmail.com")

        # Cria um mecânico a partir da mesma pessoa
        mecanico = Mecanico(pessoa)
        # Verifica se o mecânico tem o nome correto
        self.assertEqual(mecanico.pessoa.nome, "João da Silva")

        # Cria um serviço
        servico = Servico("Troca de óleo", 150)
        # Verifica se os atributos do serviço estão corretos
        self.assertEqual(servico.descricao, "Troca de óleo")
        self.assertEqual(servico.valor, 150)

        # Cria um veículo do tipo carro
        veiculo = Carro("ABC-1234", "Preto", 5, 4)
        # Verifica se os atributos do veículo estão corretos
        self.assertEqual(veiculo.placa, "ABC-1234")
        self.assertEqual(veiculo.cor, "Preto")

        # Cria um serviço realizado (liga serviço e mecânico)
        servico_realizado = ServicoRealizado(servico, mecanico)
        # Verifica se a descrição do serviço realizado está correta
        self.assertEqual(servico_realizado.servico.descricao, "Troca de óleo")

        # Cria uma ordem de serviço completa
        ordem = OrdemServico(
            date(2024, 1, 1),   # data de entrada
            veiculo,            # veículo
            date(2024, 1, 2),   # data de saída
            cliente,            # cliente
            10,                 # desconto
            servico_realizado   # serviço realizado
        )

        # Verifica se os atributos da ordem de serviço estão corretos
        self.assertEqual(ordem.cliente.email, "josilva@gmail.com")
        self.assertEqual(ordem.veiculo.placa, "ABC-1234")
        self.assertEqual(ordem.desconto, 10)


# Executa os testes quando o arquivo é rodado diretamente
if __name__ == "__main__":
    unittest.main()
