class ComponenteUI:
    def __init__(self, posicion, dimension):
        self.posicion = posicion
        self.dimension = dimension

    def render(self):
        print(self.posicion)
        print(self.dimension)

class boton(ComponenteUI):
    def __init__(self, posicion, dimension, color):
        super().__init__(posicion, dimension)
        self.color = color
        
    def hacer_click():
        print("ha hecho click")