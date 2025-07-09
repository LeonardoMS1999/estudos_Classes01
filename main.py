from datetime import date
ano_atual = date.today().year

class Carro:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def apresentar(self):
        print('---------------------------------------------')
        print(f'Marca : {self.marca}, Modelo : {self.modelo}')
        print(f'Ano : {self.ano}, Cor : {self.cor}')
        if ano_atual - self.ano >= 30:
            print(f'Este ano não paga mais IPVA')


carro1 = Carro("GM","OPALA",1988,"OGW4128")
carro1.apresentar()


carro2 = Carro("FIAT","PUNTO",2012,"EYH6E42")
carro2.apresentar()