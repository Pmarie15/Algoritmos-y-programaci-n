from datetime import datetime

def calcular_edad():
   
    año_actual = datetime.now().year
    
    nombre = input("Ingrese su nombre: ")
    apellido = input("ingrese su apellido: ")
    año_nacimiento = int(input("Ingrese su año de nacimiento: "))

    edad = año_actual - año_nacimiento

    
    print(f"{nombre} {apellido} debe cumplir o cumplió {edad} años este año.")

calcular_edad()