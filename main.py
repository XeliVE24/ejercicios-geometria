from lib import *


obj_rect= rectangulo(10,5)
print (obj_rect)
print(obj_rect.ancho)

print("ancho:"+str(obj_rect.ancho))    
print("largo:"+str(obj_rect.largo))

obj_rect2= rectangulo(25,15)
print (obj_rect2)
print(obj_rect2.ancho)

print("ancho:"+str(obj_rect2.ancho))    
print("largo:"+str(obj_rect2.largo))


obj_rect3= rectangulo(0,0)
obj_rect3.ancho=75
obj_rect3.largo=55
print("ancho:"+str(obj_rect3.ancho)+"[cm]")    
print("largo:"+str(obj_rect3.largo)+"[cm]")

print("perimetro rec1:"+str(obj_rect.perimetro()))
print("area rec1:"+str(obj_rect.area()))