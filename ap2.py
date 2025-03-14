import math

def angulos(lado_1,lado_2,lado_3):
    global angulo_a,angulo_b,angulo_c
    angulo_a=math.degrees(math.acos((lado_2**2+lado_3**2-lado_1**2)/(2*lado_2*lado_3)))
    angulo_b =math.degrees(math.acos((lado_1**2+lado_3**2-lado_2**2)/(2*lado_1*lado_3)))
    angulo_c =math.degrees(math.acos((lado_1**2+lado_2**2-lado_3**2)/(2*lado_1*lado_2)))
    print(f"Angulo a: {angulo_a:.2f}° Angulo b: {angulo_b:.2f}° Angulo c: {angulo_c:.2f}°")
    return angulo_a,angulo_b,angulo_c
def tp_tri_lado(lado_1,lado_2,lado_3):
    if lado_1==lado_2==lado_3:
        print("Equilatero")
    elif lado_1!=lado_2==lado_3 or lado_1==lado_2!=lado_3 or lado_1==lado_3!=lado_2:
        print("Isoseles")
    elif lado_1!=lado_2!=lado_3:
        print("Escaleno")

def tp_tri_angulos(angulo_a,angulo_b,angulo_c):
    if angulo_a==90 or angulo_b==90 or angulo_c==90:
        print("Rectangulo")
    elif angulo_a>90 or angulo_b>90 or angulo_c>90:
        print("Obtusangulo")
    else:
        print(f"Acutangulo {angulo_b}")

while True:
    lado_1=int(input("Ingrese el primer lado: "))
    lado_2=int(input("Ingrese el segundo lado: "))
    lado_3=int(input("Ingrese el tercer lado: "))
    
    if lado_1+lado_2<=lado_3 or lado_1+lado_3<=lado_2 or lado_2+lado_3<=lado_1:
        print("No es un triangulo")
    else:
        angulos(lado_1,lado_2,lado_3)
        tp_tri_lado(lado_1,lado_2,lado_3)
        tp_tri_angulos(angulo_a,angulo_b,angulo_c)
   