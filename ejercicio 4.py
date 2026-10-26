class Pago:
    def __init__(self, codigo, titular, monto):
        self.codigo = codigo
        self.titular = titular
        self.monto = monto

    def calcular_comision(self):
        return 0

    def total_a_cobrar(self): 
        return self.monto + self.calcular_comision()

    def __str__(self):
        return f"Código: {self.codigo} | Titular: {self.titular} | Monto: {self.monto} | Comisión: {self.calcular_comision()} | Total: {self.total_a_cobrar()}"

class PagoTarjeta(Pago):
    def __init__(self, codigo, titular, monto, num_cuotas):
        super().__init__(codigo, titular, monto)
        self.num_cuotas = num_cuotas

    def calcular_comision(self):
            return self.monto * 0.03 + 300 * self.num_cuotas


class PagoPSE(Pago):
    def __init__(self, codigo, titular, monto, banco):
        super().__init__(codigo, titular, monto)
        self.banco = banco

    def calcular_comision(self):
            return 1500

class PagoBilletera(Pago):
    def __init__(self, codigo, titular, monto, billetera):
         super().__init__(codigo, titular, monto)
         self.billetera = billetera
    def calcular_comision(self):
        if self.monto < 50000:
             return 0
        else:
             return self.monto * 0.01
pagos = []          
def buscar_pago(codigo):
     for info in pagos:
          if info.codigo == codigo:
               return info
     return None
def valor_monto(monto):
     if monto <= 0:
          return False
     return True

def crear_pago(metodo, codigo, titular, monto):
     if metodo == 1:
          while True:
               num_cuotas = int(input("diga el numero de cuotas: "))
               if num_cuotas > 0:
                    return PagoTarjeta(codigo, titular, monto, num_cuotas)
               print("numero de cuotas no valido")

     elif metodo == 2:
          banco = input("diga el nombre el banco: ").lower()
          return PagoPSE(codigo, titular, monto, banco)

     elif metodo == 3:
          billetera = input("diga el nombre de la billetera a la que quiere depositar: ").lower()
          return PagoBilletera(codigo, titular, monto, billetera)
     return False

def total_comisiones():
     for historial in pagos:
          for comision in historial:
               print(comision)  
     
while True:
     seleccion = input("1. Registrar un pago (el usuario elige el método: tarjeta, PSE o billetera).\n2. Ver todos los pagos con su comisión y total.\n3. Ver el total recaudado y el total de comisiones.\n4. Buscar un pago por código y mostrar su detalle.\n5. Salir.\nelija una opcion: ")
     if seleccion == "1":
        codigo = int(input("Código del pago: "))
        if buscar_pago(codigo) :
            print("Ese código ya existe.")
        else: 
          titular = input("diga el nombre del titular de la cuenta: ")
          monto = int(input("diga el valor del monto:"))
          if valor_monto(monto):
               metodo = int(input("1. Pago tarjeta\n2. Pago PSE\n3. Pago Billetera\nseleccione un metodo de pago: "))
               pago = crear_pago(metodo, codigo, titular, monto)
               if pago:
                    pagos.append(pago)
                    print("pago registrado")
               else:
                    print("metodo no valido")
          else:
               print("monto no aceptado: ")

     elif seleccion == "2":
          if not pagos:
               print("No hay pagos registrados.")
          for p in pagos:
               print(p)
               
     elif seleccion == "3":
          total_comisiones()

     elif seleccion == "4":
          pass
     elif seleccion == "5":
          pass
     else:
          pass
     