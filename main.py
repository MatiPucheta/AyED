

import sys
55
def salir():
    sys.exit(0)

def sep():
    return print("_"*50)

user = "administrador"
contraseña = "12345"


inicio = input("Bienvenido estimado, ¿le interesaría ingresar al programa? (conteste con 'Si' o 'No'): ")

respuesta = inicio.lower()


intentos = 0


if respuesta == "si":
    while intentos < 4:
        
        login_user = input("Ingrese su nombre de usuario: ")
        
        login_contra = str(input("Ingrese su contraseña: "))
        
        if user == login_user and contraseña == login_contra:
            
            print("Felicidades has podido ingresar!")
            
            break
        else:
            print("Usuario o contraseña incorrectos. Intenta nuevamente.")
            
            intentos += 1
            
    if intentos == 4:
        
        input("Lo lamentamos pero has fallado 3 veces, y debido a medidas de seguridad el programa se cerrará.")
        
        salir()
else: 
    input("Entonces que tenga un buen día, hasta luego: ")
    
    salir()




sep()


menú = {
    1: "Gestion de locales",
    2: "Crear cuentas de dueños locales",
    3: "Aprobar / Denegar solicitud de descuento",
    4: "Gestión de novedades",
    5: "Reporte de utilización de descuentos",
    0: "Salir"
}

gestión_menú = {
    "a": "Crear locales",
    "b": "Modificar local",
    "c":" Eliminar local",
    "d": "Volver"
}

print(f"Aquí se le mostrará el menú principal: {menú}")


while True:
    elección = int(input("¿Que parte del menú principal le gustaría ver?: ")) 
    
    if elección > 1:
        
        print("Lo lamentamos pero esta sección está en construcción")
        
    elif elección == 0: 
        
        salir()
        
    else:
        
        print(gestión_menú)
        
        while True:
            
            sub_menú = input("¿Que parte del menú de 'Gestión de Locales' le gustaría ver?: ")
            sep()
            if sub_menú == "b" or sub_menú == "c":
                print("Lo lamentamos pero esta sección está en construcción")
            
            elif sub_menú == "a":
                sep()
                
                print("Lamentamos informar se deben de almacenar 4(cuatro) locales en total si o si por ahora")
                nombres = nombre1, nombre2, nombre3, nombre4 = input("Ingrese los nombres separados por espacios por favor: ").split()
                rubros = rubro1, rubro2, rubro3, rubro4 = input("Ingrese los rubros separados por espacios acorde con el orden que los nombres: ").split()
                ubicaciones = ubicación1, ubicación2, ubicación3, ubicación4 = input("Ingrese las ubicaciones separadas por espacios acorde con el orden que los rubros: ").split()
                if rubro1 == rubro2 and rubro1 == rubro3  :
                    print(f"El rubro '{rubro1}' tiene la mayor cantidad de locales")
                elif rubro2 == rubro3 and rubro2 == rubro4:
                    print(f"El rubro '{rubro2}' tiene la mayor cantidad de locales")
                elif rubro3 == rubro4 and rubro3 == rubro1:
                    print(f"El rubro '{rubro3}' tiene la mayor cantidad de locales")
                elif rubro4 == rubro1 and rubro4 == rubro2:
                    print(f"El rubro '{rubro4}' tiene la mayor cantidad de locales")
                elif rubro4 == rubro2 and rubro4 == rubro3:
                    print(f"El rubro '{rubro2}' tiene la mayor cantidad de locales")
                else: 
                    print("Ningún rubro tiene más locales que el otro")
            else:
                print("Volviendo...")
                break
