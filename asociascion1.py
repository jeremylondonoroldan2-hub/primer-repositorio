class DocumentoDatos:
    def __init__(self, titulo, ventas):
        self.titulo = titulo
        self.ventas = ventas

class ExportadorPDF:
    def __init__(self, tamaño_pagina="A4"):
        self.tamaño_pagina = tamaño_pagina

    def generar_pdf(self, documento):
        print(documento.titulo)
        print(self.tamaño_pagina)
        for mes, ventas in documento.ventas.items():
            print(f"{mes}:{ventas}")
     
       


