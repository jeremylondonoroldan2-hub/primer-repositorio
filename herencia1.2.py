class ComponenteUI:
    def __init__(self, posicion, dimension):
        self.posicion = posicion
        self.dimension = dimension

    def render

class NotificacionEmail(Notificacion):
    def __init__(self, destinatario, mensaje, asunto, archivo):
        super().__init__( destinatario, mensaje)
        self.asunto = asunto
        self.archivo = []

    def adjuntar_archivo(self, archivo):
        self.archivo.append(archivo)

class NotificacionSMS(Notificacion):
    def __init__(self, destinatario, mensaje, codigo_pais):
        super().__init__( destinatario, mensaje)
        self.codigo_pais = codigo_pais

    def validar_longitud(self):
        return len(self.mensaje) <= 160
        