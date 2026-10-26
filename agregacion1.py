class ServidorWeb:
    def __init__(self, ip, ram):
        self.ip = ip
        self.ram = ram
        self.saludable = None

class BalanceadorCarga:
    def __init__(self):
        self.servidores = []

    def registrar_servidor(self,servidor):
        self.servidores.append(servidor)

    def remover_servidor(self, servidor):
        self.servidores.remove(servidor)

    def mostrar_activos(self):
        print("===== Servidores activos =====")
        for serv in self.servidores: 
            if serv.saludable:
                print(f"{serv.ip} - {serv.ram}GB RAM")
        print("==============================")


