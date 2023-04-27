#librería importada para la contraseña oculta
import getpass

#módulo para calcular el rubro con menos locales
def menorLocal():
    if comida == indumentaria and comida == perfumería:
        print("Ningún rubro tiene menos locales que los demás.")
    elif comida < indumentaria and comida < perfumería:
        print(f"El rubro con menos locales es 'comida', con {comida} locales")
    elif indumentaria < comida and indumentaria < perfumería:
        print(f"El rubro con menos locales es 'indumentaria', con {indumentaria} locales")
    elif perfumería < comida and perfumería < indumentaria:
        print(f"El rubro con menos locales es 'perfumería', con {perfumería} locales")
    elif comida == indumentaria:
        print("Los rubros 'comida' e 'indumentaria' tienen la misma cantidad de locales.")
    elif indumentaria == perfumería :
        print("Los rubros 'indumentaria' y 'perfumería' tienen la misma cantidad de locales.")
    elif comida == perfumería:
        print("Los rubros 'comida' y 'perfumería' tienen la misma cantidad de locales.")

#módulo para calcular el rubro con más locales
def mayorLocal():
    if comida == indumentaria and comida == perfumería:
        print("Ningún rubro tiene más locales que los demás.")
    elif comida > indumentaria and comida > perfumería:
        print(f"El rubro con más locales es 'comida', con {comida} locales")
    elif indumentaria > comida and indumentaria > perfumería:
        print(f"El rubro con más locales es 'indumentaria', con {indumentaria} locales")
    elif perfumería > indumentaria and perfumería > comida:
        print(f"El rubro con más locales es 'perfumería', con {perfumería} locales")
    elif comida == indumentaria:
        print("Los rubros 'comida' e 'indumentaria' tienen la misma cantidad de locales.")
    elif indumentaria == perfumería :
        print("Los rubros 'indumentaria' y 'perfumería' tienen la misma cantidad de locales.")
    elif comida == perfumería:
        print("Los rubros 'comida' y 'perfumería' tienen la misma cantidad de locales.")

#separador a fin de estética
def sep():
    return print("-"*70)


#constantes
nombreUsuario = "admin@shopping.com"
claveUsuario = "12345"

#bienvenida
inicio = input("Bienvenido estimado, ¿le interesaría ingresar al programa? (conteste con 'Si' o 'No'): ")

#se convierte al input a minúscula
respuesta = inicio.lower()

#contador
intentos = 0

#variables booleanas (utilizadas para evitar un loop)
terminar = False
finalizar = False
parar = False
concluir = False


#menú principal
menú_principal = ("""1: Gestion de locales
2: Crear cuentas de dueños de locales
3: Aprobar / Denegar solicitud de descuento
4: Gestión de novedades
5: Reporte de utilización de descuentos
0: Salir""""")

#menú de gestión de locales
gestión_menú = ("""a: Crear locales
b: Modificar local
c: Eliminar local
d: Volver""")


#contadores de los rubros
comida = 0
indumentaria = 0
perfumería = 0

#programa principal

if respuesta == "si" or respuesta == "sí": #logeo
    
    while not concluir:  #verificación del tipo de usuario
        
        clase_user = int(input("""¿Quién es usted?
1. Administrador
2. Dueño de local
3. Cliente
Elija el tipo de usuario con el que quiere ingresar: """))
        if clase_user == 1:
            print("Bienvenido Administrador!")
            concluir = True
        elif clase_user == 2 or clase_user == 3:
            print("En construcción...")
        elif clase_user != 1:
            print("Opción inválida.")
        sep()

    while not terminar:         
        login_user = input("Ingrese su nombre de usuario: ")
        login_pass = getpass.getpass("Ingrese su contraseña: ")
        
        if nombreUsuario == login_user and claveUsuario == login_pass:
            print("Felicidades, has podido ingresar!")
            sep()
            print("Aquí se le mostrará el menú principal: ")
            
            print(menú_principal)
            sep()
            while not finalizar: #menú principal
                #variable booleana
                terminar = False
                
                elección = int(input("¿Que parte del menú principal le gustaría ver?: "))
                
                if elección == 2 or elección == 3 or elección == 4 or elección == 5:
                    print("Lo lamentamos pero esta sección está en construcción")
                
                elif elección > 5 or elección < 0:
                    sep()
                    print("Opción inválida. Eliga una de las opciones disponibles.")
                    
                elif elección == 1:
                    sep()
                    print(gestión_menú)
                    
                    while not terminar: #menú gestion de locales
                        sub_menú = input("¿Que parte del menú de 'Gestión de Locales' le gustaría ver?: ").lower()
                        sep()
                        if sub_menú == "b" or sub_menú == "c":
                            print("Lo lamentamos pero esta sección está en construcción")
                        
                        elif sub_menú == "a":
                            sep()
                            #variable booleana
                            parar = False
                            
                            print("Ingrese los datos de los locales que desee crear (máximo tres)")
                            
                            nombreLocal = nombre1, nombre2, nombre3 = input("Ingrese los nombres separados por comas, por favor: ").split(",")
                            
                            #verificación de los rubros
                            while not parar:
                                rubroLocal = rubro1, rubro2, rubro3 = input("Ingrese los rubros separados por espacios acorde al orden de su nombre: ").split()
                                if rubro1 == "comida" or rubro1 == "indumentaria" or rubro1 == "perfumería":
                                    if rubro2 == "comida" or rubro2 == "indumentaria" or rubro2 == "perfumería":
                                        if rubro3 == "comida" or rubro3 == "indumentaria" or rubro3 == "perfumería":
                                            parar = True
                                        else: print("Algún rubro ingresado no es válido")
                                    else: print("Algún rubro ingresado no es válido")
                            
                            ubicacionLocal = ubi_1, ubi_2, ubi_3 = input("Ingrese las ubicaciones separadas por comas acorde al orden de su rubro: ").split(",")
                            
                            #se cuenta cuantas veces los rurbos fueron ingresados
                            for rubro in rubroLocal:
                                if rubro == "comida":
                                    comida += 1
                                elif rubro == "indumentaria":
                                    indumentaria += 1
                                elif rubro == "perfumería":
                                    perfumería += 1
                            
                            mayorLocal()
                            menorLocal()
                        
                        elif sub_menú != "d": #verificación
                            print("Opción inválida. Eliga una de de las opciones disponibles.")
                        
                        else:
                            print("Volviendo...")
                            terminar = True
                            
                else: #se corta el loop del menú principal y del de logeo
                    finalizar = True
                    terminar = True
                    input("Que tenga un buen día, hasta luego") #mensaje de despedida
                            
        else: #se suman los intentos
            intentos += 1
            if intentos < 3:
                print("Usuario o contraseña incorrectos. Intenta nuevamente.")
            
        if intentos == 3: #si los intentos inválidos son 3, se cierra el programa
            input("Lo lamentamos pero has fallado 3 veces, y debido a medidas de seguridad el programa se cerrará.")
            terminar = True
            
else: #mensaje de despedida 
    input("Entonces que tenga un buen día, hasta luego")



