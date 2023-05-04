#librería importada para la contraseña oculta
import getpass

#variables booleanas (utilizadas para evitar un loop)
concluir = False
finalizar = False
terminar = False
parar = False
acabar = False  

#contadores de los rubros
comida = 0
indumentaria = 0
perfumería = 0

#constantes
nombreUsuario = "admin@shopping.com"
claveUsuario = "12345"

#contador
intentos = 0

#menú principal
menú_principal = ("""1: Gestion de locales
2: Crear cuentas de dueños de locales
3: Aprobar / Denegar solicitud de descuento
4: Gestión de novedades
5: Reporte de utilización de descuentos
0: Salir""")

#menú de gestión de locales
gestión_menú = ("""a: Crear locales
b: Modificar local
c: Eliminar local
d: Volver""")

#menú de gestión de novedades
novedades_menú = ("""a: Crear novedades
b: Modificar novedad
c: Eliminar novedad
d: Ver reporte de novedades
e: Volver""")   

#separador a fin de estética
def sep():
    return print("-"*70)

#MÓDULO del menú principal
def menuPrincipal():
    global terminar, finalizar
    while not finalizar:         
        elección = int(input("¿Que parte del menú principal le gustaría ver?: "))

        if elección == 2 or elección == 3 or elección == 5:
            print("Lo lamentamos pero esta sección está en construcción")

        elif elección == 4:
            menuGestionNov()

        elif elección > 5 or elección < 0:
            sep()
            print("Opción inválida. Eliga una de las opciones disponibles.")

        elif elección == 1:
            sep()
            menuGestionLocales()

        else:
            finalizar = True
            terminar = True
            input("Que tenga un buen día, hasta luego") #mensaje de despedida

#MÓDULO de la sección Gestión de Novedades
def menuGestionNov():
    global acabar
    sep()
    print(novedades_menú)        
    while not acabar:
        sub_menu_4 = input("¿Qué parte del menú de 'Gestión de novedades' le gustaría ver?: ").lower()
        sep()    
        if sub_menu_4 == "a" or sub_menu_4 == "b" or sub_menu_4 == "c" or sub_menu_4 == "d":
            print("Lo lamentamos pero esta sección está en construcción")
        elif sub_menu_4 != "e":
            print("Opción inválida. Elija una de las opciones disponibles.")
        else:
            print("Volviendo...")
            acabar = True

#MÓDULO de la sección Gestión de Locales
def menuGestionLocales():
    global terminar, parar
    print(gestión_menú)
    while not terminar: #menú gestion de locales
        sub_menu_1 = input("¿Que parte del menú de 'Gestión de Locales' le gustaría ver?: ").lower()
        sep()
        if sub_menu_1 == "b" or sub_menu_1 == "c":
            print("Lo lamentamos pero esta sección está en construcción")

        elif sub_menu_1 == "a":
            sep()
            #variable booleana
            parar = False

            print("Ingrese los datos de los locales que desee crear (máximo tres)")
            global nombreLocal, nombre1, nombre2, nombre3
            nombreLocal = nombre1, nombre2, nombre3 = input("Ingrese los nombres separados por comas, por favor: ").split(",")
            
            #verificación de los rubros
            while not parar:
                global rubroLocal
                rubroLocal = rubro1, rubro2, rubro3 = input("Ingrese los rubros separados por espacios acorde al orden de su nombre: ").split()
                if rubro1 == "comida" or rubro1 == "indumentaria" or rubro1 == "perfumería":
                    if rubro2 == "comida" or rubro2 == "indumentaria" or rubro2 == "perfumería":
                        if rubro3 == "comida" or rubro3 == "indumentaria" or rubro3 == "perfumería":
                            parar = True
                        else: print("Algún rubro ingresado no es válido")
                    else: print("Algún rubro ingresado no es válido")
            global ubicacionLocal, ubi_1, ubi_2, ubi_3
            ubicacionLocal = ubi_1, ubi_2, ubi_3 = input("Ingrese las ubicaciones separadas por comas acorde al orden de su rubro: ").split(",")

            calcLoc()

        elif sub_menu_1 != "d": #verificación
            print("Opción inválida. Eliga una de de las opciones disponibles.")

        else:
            print("Volviendo...")
            menuPrincipal()

#MÓDULO para calcular los locales de los rubros
def calcLoc():
    global rubroLocal
    global comida, indumentaria, perfumería
    #se cuenta cuantas veces los rurbos fueron ingresados
    for rubro in rubroLocal:
        if rubro == "comida":
            comida += 1
        elif rubro == "indumentaria":
            indumentaria += 1
        elif rubro == "perfumería":
            perfumería += 1
    
    if comida == indumentaria and comida == perfumería:
        print("Ningún rubro tiene menos locales que los demás.")
    elif comida < indumentaria and comida < perfumería:
        print(f"El rubro con menos locales es 'comida', con {comida} locales")
    elif indumentaria < comida and indumentaria < perfumería:
        print(f"El rubro con menos locales es 'indumentaria', con {indumentaria} locales")
    elif perfumería < comida and perfumería < indumentaria:
        print(f"El rubro con menos locales es 'perfumería', con {perfumería} locales")
    elif comida == indumentaria:
        print(f"Los rubros 'comida' e 'indumentaria' tienen la misma cantidad de locales, con {comida} locales.")
    elif indumentaria == perfumería :
        print(f"Los rubros 'indumentaria' y 'perfumería' tienen la misma cantidad de locales, con {indumentaria} locales.")
    elif comida == perfumería:
        print(f"Los rubros 'comida' y 'perfumería' tienen la misma cantidad de locales, con {perfumería} locales.")
    
    if comida == indumentaria and comida == perfumería:
        print("Ningún rubro tiene más locales que los demás.")
    elif comida > indumentaria and comida > perfumería:
        print(f"El rubro con más locales es 'comida', con {comida} locales")
    elif indumentaria > comida and indumentaria > perfumería:
        print(f"El rubro con más locales es 'indumentaria', con {indumentaria} locales")
    elif perfumería > indumentaria and perfumería > comida:
        print(f"El rubro con más locales es 'perfumería', con {perfumería} locales")
    elif comida == indumentaria:
        print(f"Los rubros 'comida' e 'indumentaria' tienen la misma cantidad de locales, con {comida} locales.")
    elif indumentaria == perfumería :
        print(f"Los rubros 'indumentaria' y 'perfumería' tienen la misma cantidad de locales, con {indumentaria} locales.")
    elif comida == perfumería:
        print(f"Los rubros 'comida' y 'perfumería' tienen la misma cantidad de locales, con {perfumería} locales.")


#PROGAMA PRINCIPAL

#bienvenida
inicio = input("Bienvenido estimado, ¿le interesaría ingresar al programa? (conteste con 'Si' o 'No'): ")

#se convierte al input a minúscula
respuesta = inicio.lower()

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

    while not terminar:   #verificación del usuario y contraseña
        login_user = input("Ingrese su nombre de usuario: ")
        login_pass = getpass.getpass("Ingrese su contraseña: ")
        
        if nombreUsuario == login_user and claveUsuario == login_pass:
            print("Felicidades, has podido ingresar!")
            sep()
            print("Aquí se le mostrará el menú principal: ")
            print(menú_principal)
            sep()
            menuPrincipal()
            
        else: #se suman los intentos
            intentos += 1
            if intentos < 3:
                print("Usuario o contraseña incorrectos. Intenta nuevamente.")
            
        if intentos == 3: #si los intentos inválidos son 3, se cierra el programa
            input("Lo lamentamos pero has fallado 3 veces, y debido a medidas de seguridad el programa se cerrará.")
            terminar = True
            
else: #mensaje de despedida 
    input("Entonces que tenga un buen día, hasta luego")



