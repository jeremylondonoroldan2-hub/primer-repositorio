class PaqueteCodigo:
    def __init__(self, nombre, version, rama):
        self.nombre = nombre
        self.version = version
        self.rama = rama

class ServidorDespliegue:
    def __init__(self,ip, entorno):
        self.ip = ip
        self.entorno = entorno

    def desplegar(self, servidor):
        