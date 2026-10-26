class Notificacion:
    def __init__(self, destinatario, mensaje):
        self.destinatario = destinatario
        self.mensaje = mensaje

    def registrar_fecha_envio(self, fecha):
        self.fecha = None

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
        