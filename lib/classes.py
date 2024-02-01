#class rectangulo:
 "   def __init__(self, largo ,ancho):
  #    self.largo = largo
 #      return 2*(self.largo + self.ancho)
# self.ancho = ancho
    #    pass 

   # def __str__(self):
   #     return f"rectangulo de largo {self.largo} ancho {self.ancho}"
    
        
   # def area(self):
   #     return (self.largo * self.ancho)
  #  def perimetro(self):
   class articulo:
    def __init__(self,idArt,marca,nombre,precio=None,peso=None,descuento=None,inv=None):
        self.idArt= idArt
        self.marca=marca
        self.nombre=nombre
        self.peso=peso
        self.descuento=descuento
        self.precio=precio
        self.inv=inv

        pass
    def __str__(self):
         return f"idArt:{self.idArt}- marca : {self.marca}-precio{self.precio}-peso{self.peso}-descuento{self.descuento}-inv{self.inv}-precioDcto{self.preciocto}"
    
    def setPrecio(self,precio):
        self.precio=precio
        return 0
        
    def setPeso(self,peso):
        self.peso=peso
        return 0
    
    def setInv(self,inv):
        self.inv=inv
        return 0
    
        
    def setDcto(self,descuento):
        self.descuento=descuento
        return 0
    
    def getPreciodto(self):
        if self.descuento != None:
            precioDcto=self.precio-(self.precio*(self.descuento/100))
        else:
            precioDcto=self.precio
        return precioDcto
    
    
  
class carrito ():
    def __init__(self,idCart):
        self.idCart=idCart
        self.articulos= []
        pass
    
    def __str__(self):
        printCarrito=f"carrito:{self.idCart}"
        if len(self.articulos)>=1:
            for i in range (0,len(self.articulos),1):
             printCarrito += f"Articulo:{self.articulos[i]}\n"
        else :
                printcarrito+=f"carrito vacio"
                return printCarrito
    

    def addArticulos(self,idArt):
        self.articulos.append(idArt)
        return 0 
    pass     
