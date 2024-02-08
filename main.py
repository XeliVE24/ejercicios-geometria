from lib import *


#obj_rect= rectangulo(10,5)
#print (obj_rect)
#print(obj_rect.ancho)

#print("ancho:"+str(obj_rect.ancho))    
#print("largo:"+str(obj_rect.largo))

#obj_rect2= rectangulo(25,15)
#print (obj_rect2)
#print(obj_rect2.ancho)
"""
#print("ancho:"+str(obj_rect2.ancho))    
print("largo:"+str(obj_rect2.largo))


obj_rect3= rectangulo(0,0)
obj_rect3.ancho=75
obj_rect3.largo=55
print("ancho:"+str(obj_rect3.ancho)+"[cm]")    
print("largo:"+str(obj_rect3.largo)+"[cm]")

print("perimetro rec1:"+str(obj_rect.perimetro()))
print("area rec1:"+str(obj_rect.area()))"""
""""""###


#obj_poly_1=poligono(5,18)
#print(obj_poly_1)
#print(f"num Lados:{obj_poly_1.numLado}")
#print(obj_poly_1.nomPoly())



obj_poly_2=PoligonoRegular(5,10,15)
print(obj_poly_2)
print(obj_poly_2.nomPoly())
print(obj_poly_2.periPoly())
print(f"el area de un poligono :{obj_poly_2.getArea()}")
print(f"el area es mayor a 200??{obj_poly_2.chkArea()}")
obj_poly_2.setcolor("azul")
print(obj_poly_2.color)

#    ------------------------------------------------
ZeroDivisionError
num1 =10
num2=0

try:
    div = num1/num2
#"""except ZeroDivisionError:
   # print("no puedes dividir entre 0 ")
#except TypeError :
   # print("no puedes dividir str entre numeros ")"""
except Exception as e:
    print(f"error desconocido:{e}")


#----------------------------------------
print ("hellow")
print ("este es otro commit")

#-----------------------------------------------------------

art1 = Articulo(10256,"Coca-Cola","Canada Dry")
art1.setDescuento(10)
art1.setPeso(10)
art1.setInventario(10)
art1.setPrecio(25.00)
print(art1)
cart1 = Cart("ABC123")
#print(cart1)
cart2 = Cart("DEF456")
#print(cart2)
cart3 = Cart("GHI789")

art2 = Articulo(10165,"Sabritas","sabor limon  500gr")
art1.setDescuento(25)
art1.setPeso(500)
art1.setInventario(5)
art1.setPrecio(22.00)
art2.setDescuento(25)
art2.setPeso(500)
art2.setInventario(5)
art2.setPrecio(22.00)
#print(art2)

art3 = Articulo(11608,"La Rosa ","mazapan ")
art1.setPeso(150)
art1.setInventario(5)
art1.setPrecio(22.00)
art3.setPeso(150)
#art3.setInventario(5)
art3.setPrecio(22.00)
#print(art3)

cart1.addarticulo(art1.Id)
cart1.addarticulo(art2.Id)
cart1.addarticulo(art3.Id)
cart1.addarticulo(art1)
cart1.addarticulo(art2)
cart1.addarticulo(art3)
print(cart1)
print(cart2)
print("---------------------------------")
print(cart1.objArticulos[0])
print(cart1.objArticulos[0].nombre)
print(cart1.objArticulos[1].nombre)
print(art1.inventario)
print(art2.inventario)
print(art3.inventario)
print("--------------------------------------")
print(f"Carrito: {cart1.IdCart}\nTotal: { cart1.getTotal1()}")