#class rectangulo:
# "   def __init__(self, largo ,ancho):
  #    self.largo = largo
 #      return 2*(self.largo + self.ancho)
# self.ancho = ancho
    #    pass 

   # def __str__(self):
   #     return f"rectangulo de largo {self.largo} ancho {self.ancho}"
    
        
   # def area(self):
   #     return (self.largo * self.ancho)
  #  def perimetro(self):
# INICIO ARTICULO        
class Articulo():
    def __init__(self,marca,nombre,Id,precio=None,peso=None,descuento=None,inventario=None):
        self.marca = marca
        self.nombre = nombre
        self.precio = precio
        self.peso = peso
        self.descuento = descuento
        self.Id = Id
        self.inventario = inventario
        pass
    def __str__(self):
        return f"nombre: {self.Id} | Id: {self.marca} | marca: {self.nombre} | Precio: {self.precio} | Peso: {self.peso} | descuento: {self.descuento} | inventario: {self.inventario}"
        
    def setPrecio(self,precio):
        self.precio = precio
        return 0
    
    def setPeso(self,peso):
        self.peso  = peso
        return 0
    def setDescuento(self,descuento):
        self.descuento = descuento
        return 0
    def setInventario(self,inventario):
        self.inventario = inventario
        return 0
    def getDescuento(self):
        if self.descuento != None:
            precioDescuento = (self.precio * (self.descuento/100))
        else:
            precioDescuento = 0
        return precioDescuento    
        
    def getPreciodto(self):
        if self.descuento != None:
            precioDescuento = self.precio - (self.precio * (self.descuento/100))
        else:
            precioDescuento = self.precio    
        return precioDescuento    
        
    
        
# FIN ARTICULO        
class Cart():
    def __init__(self,IdCart):
        self.IdCart = IdCart
        self.objArticulos =[ ]
        pass
        
    def __str__(self):
        printCart = f"Ticket# : {self.IdCart} \n"
        if len(self.objArticulos) >= 1:
            for i in range (0, len(self.objArticulos),1):
                printCart += f"{self.objArticulos[i].Id} {self.objArticulos[i].nombre} $ {self.objArticulos[i].precio} mxn\n -${self.objArticulos[i].getDescuento()}mxn\n"
        else: 
                printCart += f"Carrito vacio"    
        return printCart    
    def addarticulo(self,objArt):
        if type (objArt.inventario) != type(None):
            if objArt.inventario >= 1:
                objArt.inventario -= 1
                self.objArticulos.append(objArt)
            else:
                print(f"No hay inventario de :( {objArt.nombre}")
        else:
            print("Inventario no definido")
        return 0 
    
    def getTotal(self):
        total = 0
        for i in range (0, len(self.objArticulos),1):
            total += self.objArticulos[1].getPreciodto()
        return total
       
    def getTotalDesc(self):
        total = 0
        for i in range (0, len(self.objArticulos),1):
            total += self.objArticulos[1].getDescuento()
        return total
        
        