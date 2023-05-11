#librería importada para la contraseña oculta
import getpass


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
menú_principal = ("""-- Menú Principal --
    1: Gestion de locales
    2: Crear cuentas de dueños de locales
    3: Aprobar / Denegar solicitud de descuento
    4: Gestión de novedades
    5: Reporte de utilización de descuentos
    0: Salir""")

#menú de gestión de locales
gestión_menú = ("""-- Gestión de Locales --
    a: Crear locales
    b: Modificar local
    c: Eliminar local
    d: Volver""")

#menú de gestión de novedades
novedades_menú = ("""-- Gestión de Novedades --
    a: Crear novedades
    b: Modificar novedad
    c: Eliminar novedad
    d: Ver reporte de novedades
    e: Volver""")   

#separador a fin de estética
def sep():
    return print("-"*70)

#MÓDULO del menú principal
def menuPrincipal():
    global intentos
    
    print(menú_principal)
    sep()
    
    elección = int(input("¿Que parte del menú principal le gustaría ver?: "))
    while elección != 0:
        
        
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
        
        sep()
        elección = int(input("¿Que parte del menú principal le gustaría ver?: "))
    intentos = 3
    input("Que tenga un buen día, hasta luego") #mensaje de despedida

#MÓDULO de la sección Gestión de Novedades
def menuGestionNov():
    sep()
    print(novedades_menú)
    
    sub_menu_4 = input("¿Qué parte del menú de 'Gestión de novedades' le gustaría ver?: ").lower()        
    while sub_menu_4 != "e":
        
        sep()    
        if sub_menu_4 == "a" or sub_menu_4 == "b" or sub_menu_4 == "c" or sub_menu_4 == "d":
            print("Lo lamentamos pero esta sección está en construcción")
        else:
            print("Opción inválida. Elija una de las opciones disponibles.")
        
        sub_menu_4 = input("¿Qué parte del menú de 'Gestión de novedades' le gustaría ver?: ").lower()
        
    print("Volviendo...")
    sep()
    print(menú_principal)
    sep()


#MÓDULO de la sección Gestión de Locales
def menuGestionLocales():
    print(gestión_menú)
    
    sub_menu_1 = input("¿Que parte del menú de 'Gestión de Locales' le gustaría ver?: ").lower()
    while sub_menu_1 != "d": #menú gestion de locales
        
        global nombreLocal
        global ubicacionLocal
        global rubroLocal
        global comida, indumentaria, perfumería
        
        
        sep()
        if sub_menu_1 == "b" or sub_menu_1 == "c":
            print("Lo lamentamos pero esta sección está en construcción")
        
        elif sub_menu_1 == "a":
            sep()
            
            print("A continuación, ingrese los datos del local que quiera crear: ")
            
            nombreLocal = input("Ingrese el nombre de su local, por favor (un 0 indicará fin de datos): ")
            sep()
            while nombreLocal != "0":
                
                rubroLocal = input("Ingrese el rubro del local: ")
                sep()
                
                while rubroLocal != "comida" and rubroLocal != "indumentaria" and rubroLocal != "perfumería":
                    rubroLocal = input("El rubro ingresado es inválido, intentelo de nuevo por favor: ")
                    sep()
                
                #se cuenta cuantas veces los rurbos fueron ingresados
                if rubroLocal == "comida":
                    comida += 1
                elif rubroLocal == "indumentaria":
                    indumentaria += 1
                elif rubroLocal == "perfumería":
                    perfumería += 1
                ubicacionLocal = input("Ingrese la ubicación del local: ")
                sep()
                
                nombreLocal = input("Ingrese el nombre del próximo local, por favor: ")
                sep()
            
            calcLoc()
        
        elif sub_menu_1 != "d": #verificación
            print("Opción inválida. Eliga una de de las opciones disponibles.")
        
        sub_menu_1 = input("¿Que parte del menú de 'Gestión de Locales' le gustaría ver?: ").lower()
    
    print("Volviendo...")
    sep()
    print(menú_principal)
    sep()

#MÓDULO para calcular los locales de los rubros
def calcLoc():
    global rubroLocal
    global comida, indumentaria, perfumería
    
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

#MÓDULO de verificación del tipo de usuario
def usuario():
    clase_user = int(input("""¿Quién es usted?
    1. Administrador
    2. Dueño de local
    3. Cliente
Elija el tipo de usuario que es usted por favor: """))
    while clase_user != 1:
        
        if clase_user == 2 or clase_user == 3:
            print("En construcción...")
        else:
            print("Opción inválida.")
        sep()
        
        clase_user = int(input("Elija el tipo de usuario que es usted por favor: "))
    
    print("Bienvenido Administrador!")
    sep()


#PROGAMA PRINCIPAL

#bienvenida
inicio = input("Bienvenido estimado, ¿le interesaría ingresar al programa? (conteste con 'Si' o 'No'): ")

#se convierte al input a minúscula
respuesta = inicio.lower()

if respuesta == "si" or respuesta == "sí": #logeo
    
    usuario()
    
    while intentos != 3:   #verificación del usuario y contraseña
        login_user = input("Ingrese su nombre de usuario: ")
        login_pass = getpass.getpass("Ingrese su contraseña: ")
        
        if nombreUsuario != login_user and claveUsuario != login_pass: #se suman los intentos
            intentos += 1
            
            if intentos == 3: #si los intentos inválidos son 3, se cierra el programa
                input("Lo lamentamos pero has fallado 3 veces, y debido a medidas de seguridad el programa se cerrará.")
            else:
                print("Usuario o contraseña incorrectos. Intenta nuevamente.")
        
        else: 
            print("Felicidades, has podido ingresar!")
            sep()
            menuPrincipal()
        
else: #mensaje de despedida en caso de no querer logear
    input("Entonces que tenga un buen día, hasta luego")



