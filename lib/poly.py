class poligono:
    def __init__(self,numLado,sizeLado):
        self.numLado=numLado
        self.sizeLado=sizeLado
        pass

    def __str__(self):
        return f"Numero de lados: {self.numLado} y  tamaño del lado: {self.sizeLado}"
                
    def nomPoly( self ):
        match self.numLado:
            case 3:
                return"Tu poligono es un triangulo"
            case 4:
                return"Tu poligono es un cuadrado"
            case 5:
                return"Tu poligono es un pentagono"
            case 6:
                return"Tu poligono es un hexagono"
            case 7:
                return"Tu poligono es un heptagono"
            case 8:
                return"Tu poligono es un octagono"
            case 9:
                return"Tu poligono es un enagono"
            case 10:
                return"Tu poligono es un decagono"
            case _:
                return"Tu poligono no lo identifico "
            
            
            
    def periPoly(self):
        return self.numLado * self.sizeLado
    

        
##fin clase poligono 
    
    
##inicio clase poligono regular

class PoligonoRegular( poligono ):
    def __init__(self,numLado , sizeLado, apotema):
        super().__init__(numLado,sizeLado)
        self.apotema = apotema
        pass 
    def __str__(self):
        return f"numLado:{self.numLado},sizeLado:{self.sizeLado}, apotema:{self.apotema}"
    
    def getArea (self):
        area= ((self.apotema)*(super().periPoly()))/2
        return area
    
    def chkArea(self):
        if self.getArea() >= 200:
            return "si"
        else :
            return "no"

    def setcolor(self,color):
        self.color=color
        pass
        #return f"el color es :{self.color}"
    