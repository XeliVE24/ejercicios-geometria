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


obj_poly_1=poligono(5,18)
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
