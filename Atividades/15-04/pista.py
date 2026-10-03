import time

class Veiculo:
    def __init__(self, modelo, tanque, rendimento, desenho):
        self.modelo = modelo
        self.tanque = tanque # capacidade em litros
        self.rendimento = rendimento # km/litro
        self.odometro = 0  # km/s percorridos
        self.desenho = desenho # caracteres que representam o veículo
    def andar(self):
        # atualiza o odometro
        self.odometro += self.rendimento    
        # gastou gasolina :-)
        self.tanque -= 1 # self.tanque = self.tanque - 1

class Pista:
    def __init__(self, extensao):
        self.extensao = extensao
        self.veiculos = []
    def tick(self):
        for v in self.veiculos:
            # ainda tem pista pra andaR?
            if v.odometro <= self.extensao:
                v.andar() # anda, veículo :-)

    def pista_grafica(self):
        for v in self.veiculos:
            s = "." * int(v.odometro/10)
            print(v.modelo,"(",v.odometro,"):",s,v.desenho)            

fox = Veiculo("Fox", 42, 12, "o~W~o")
biz = Veiculo("Honda Biz", 5, 40, "o-o")

indianapolis = Pista (500)
indianapolis.veiculos.append(fox)
indianapolis.veiculos.append(biz)
while True:
    indianapolis.tick() # fazer os veículos andarem
    # mostrar estado dos veículos
    #print(indianapolis.veiculos[0].modelo, "andou", indianapolis.veiculos[0].odometro)
    #print(indianapolis.veiculos[1].modelo, "andou", indianapolis.veiculos[1].odometro)
    indianapolis.pista_grafica()
    # esperar um pouco
    time.sleep(1)
    # os veículos terminaram de andar na pista?
    if indianapolis.veiculos[0].odometro >= 500 and indianapolis.veiculos[1].odometro >= 500:
        break # encerra o programa

print("Fim da corrida")
