class Carro:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def apresentar(self):
        print(f'Marca : {self.marca}, Modelo : {self.modelo}')
        print(f'Ano : {self.ano}, Cor : {self.cor}')
        if self.ano < 1995:
            print(f'Este ano não paga mais IPVA')


carro1 = Carro("GM","OPALA",1988,"OGW4128")
carro1.apresentar()