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


"obj_poly_1=poligono(5,18)
print(obj_poly_1)
print(f"num Lados:{obj_poly_1.numLado}")
print(obj_poly_1.nomPoly())



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

art1= articulo (1024578,"coca-cola","canada dry")
art1.setPrecio(25.00)
art1.setPeso(250)
art1.setInv(10)
art1.setDcto(40)
cart1=carrito("abc456")
print(cart1)


cart=carrito("abc123")
cart1=carrito("abc456")
cart3=carrito("car3")


art2= articulo (17846,"sabritas","sabor limon ")
art2.setPrecio(20.00)
art2.setPeso(250)
art2.setInv(50)
art2.setDcto(0)
print (art2)



art3= articulo (24458976,"La Rosa ","mazapan ")
art3.setPrecio(5)
art3.setPeso(10)
art3.setInv(500)
art3.setDcto(2)
print (art3)
cart3=carrito("car3")
print(cart3)


cart.addArticulos(art1.idArt)
