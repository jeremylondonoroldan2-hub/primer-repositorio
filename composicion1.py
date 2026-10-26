class PoolConexiones:
    def __init__(self,limite):
        self.limite = limite
        self.conexiones_abiertas = 0

    def abrir_conexion(self):
        if self.conexiones_abiertas < self.limite:
            self.conexiones_abiertas += 1

    def cerrar_conexiones(self):
        self.conexiones_abiertas = 0

class GestorBaseDatos:
    def __init__(self,url):
        self.url = url
        self.pool = PoolConexiones(5)