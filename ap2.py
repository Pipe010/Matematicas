import math

lado_1=input("Ingrese el primer lado: ")
lado_2=input("Ingrese el segundo lado: ")
lado_3=input("Ingrese el tercer lado: ")

def angulos(lado_1,lado_2,lado_3):
    angulo_a=math.degrees((lado_1**2-lado_2**2-lado_3**2)/(2*lado_2*lado_3))
    angulo_b=math.degrees((lado_1**2-lado_2**2-lado_3**2)/(2*lado_2*lado_3))
    angulo_c=180-(angulo_a+angulo_b)
    return angulo_a, angulo_b, angulo_c
def resultado(angulo_a,angulo_b,angulo_c):
    print(angulo_a)
print(lado_1)