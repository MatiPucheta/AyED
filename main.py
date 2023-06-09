import os
#librería importada para la contraseña oculta
import getpass

#contador de filas
i = 1

F=50
C=5
# Lista para almacenar los locales
locales=[[" "]*C for i in range(F)]

# Código inicial para el primer local
codLocal = 1  

#contadores de los rubros
comida = 0
indumentaria = 0
perfumería = 0




#Array de 4x2 con los usarios y contraseñas
usuarios = [
    ["admin@shopping.com", "12345"],
    ["localA@shopping.com", "AAAA1111"],
    ["localB@shopping.com", "BBBB2222"],
    ["unCliente@shopping.com", "33xx33"]
]
#contador
intentos = 0

#menú del administrador
menú_Admin = ("""-- Menú Principal --
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
    d: Mapa de locales
    e: Volver""")

#menú de gestión de novedades
novedades_menú = ("""-- Gestión de Novedades --
    a: Crear novedades
    b: Modificar novedad
    c: Eliminar novedad
    d: Ver reporte de novedades
    e: Volver""")   

#menú del Dueño
menú_Dueño = ("""-- Menú Principal --
    1: Gestión de descuento
        a) Crear descuento para mi local
        b) Modificar descuento de mi local
        c) Eliminar descuento de mi local
        d) Volver
    2: Aceptar/Rechazar pedido de descuento
    3: Reporte de uso de descuentos
    0: Salir""")

#menú del cliente
menú_Cliente = ("""-- Menú Principal --
    1: Registrarme
    2: Buscar descuento en locales
    3: Solicitar descuento
    4: Ver novedades
    0: Salir""")

#separador a fin de estética
def sep():
    return print("-"*70)

#MÓDULO del menú principal Cliente
def menuCliente():
    global intentos
    print(menú_Cliente)
    sep()
    
    elección = int(input("¿Que parte del menú principal le gustaría ver?: "))
    while elección != 0:
        
        if elección not in (1,2,3,4):
            sep()
            print("Opción inválida. Eliga una de las opciones disponibles.")
        else:
            print("Lo lamentamos pero esta sección está en construcción")
            sep()
        
        elección = int(input("¿Que parte del menú principal le gustaría ver?: "))
    intentos = 3
    input("Que tenga un buen día, hasta luego") #mensaje de despedida


#MÓDULO del menú principal Dueño
def menuDueño():
    global intentos
    global operación
    print(menú_Dueño)
    sep()
    
    elección = int(input("¿Que parte del menú principal le gustaría ver?: "))
    
    while elección != 0:
        
        if elección not in (1,2,3):
            sep()
            print("Opción inválida. Eliga una de las opciones disponibles.")
            sep()
        else:
            
            if elección == 1:
                sep()
                operación = input("¿Que operación le gustaría realizar?: ").lower()
                
                while operación != "d":
                    os.system('cls')
                    while operación not in ("a", "b", "c","d"):
                        operación = input("Opción inválida. Eliga una de las opciones disponibles: ")
                    
                    if operación in ("a", "b", "c"):
                        print("Lo lamentamos pero esta sección está en construcción")
                        sep()
                        operación = input("¿Que operación le gustaría realizar?: ").lower()
                        os.system('cls')
                    
                    elif operación == "d": 
                        print("Volviendo...")
                    sep()
                    print(menú_Dueño)
                    sep()
            
            else: 
                print("Lo lamentamos pero esta sección está en construcción")
                sep()
        
        elección = int(input("¿Que parte del menú principal le gustaría ver?: "))
    intentos = 3
    input("Que tenga un buen día, hasta luego") #mensaje de despedida

#MÓDULO del menú principal Admin
def menuPrincipal():
    global intentos
    
    print(menú_Admin)
    sep()
    
    elección = int(input("¿Que parte del menú principal le gustaría ver?: "))
    while elección != 0:
        
        
        if elección not in (1,2,3,4,5):
            sep()
            print("Opción inválida. Eliga una de las opciones disponibles.")
        
        elif elección == 4:
            os.system('cls')
            menuGestionNov()
        
        elif elección == 2 or elección == 3 or elección == 5:
            print("Lo lamentamos pero esta sección está en construcción")
        
        elif elección == 1:
            os.system('cls')
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
    print(menú_Admin)
    sep()

#MÓDULO para mostrar los locales cargados
def mostrar_locales():
    global i
    print("== Locales Cargados ==")
    if i > 1:
        for p in range(1,i):
            print(f"Nombre: {locales[p][0]} | Ubicación: {locales[p][1]} | Rubro: {locales[p][2]} | Código: {locales[p][3]} | Estado: {locales[p][4]}")
    else:
        print("No se han cargado locales aún.")

#MÓDULO para ordernar los locales alfabéticamente
def Ordenar():
    for a in range(0,F-1):
        for b in range(1,F):
            primero = locales[a][0]
            segundo = locales[b][0]
            if primero[0] > segundo[0]:
                for k in range(C):
                    aux = locales[a][k]
                    locales[a][k] = locales[b][k]
                    locales[b][k] = aux

#MÓDULO para buscar dicotómicamente
def Repeticion(col,dato):
    fin=1
    for i in range(50):
        if locales[i][0] != " ":
            fin += 1
    ini=0
    
    while ini < fin:
        mid = (ini + fin)//2
        usado = locales[mid][col]
        if usado == dato:
            return mid
        
        elif usado[0] < dato[0]:
            fin = mid-1
        
        else:
            ini = mid+1

#MÓDULO para buscar secuencialmente
def Busquedasec(col,num):
    for i in range(50):
        if locales[i][col] == num:
            return i

#MÓDULO para cargar los locales
def crear_local():
    global codLocal, locales, i
    global nombreLocal
    global mostrar
    global comida, indumentaria, perfumería
    
    mostrar = input("¿Le gustaría ver los locales cargados?: ").lower()
    if mostrar in ("sí","si"):
        mostrar_locales()
    
    sep()
    nombreLocal = input("Ingrese el nombre del local (un '0' indicará fin de la carga): ")
    os.system("cls")
    
    while nombreLocal != '0':
        print("== Crear Local ==")
        
        sep()
        
        #Se verifica que el nombre no se esté ya usado
        find = True
        while find:
            pos = Repeticion(0,nombreLocal)
            if pos is None:
                locales[i][0] = nombreLocal
                find = False
            else:
                nombreLocal = input("El nombre del local ya existe, introduzca uno no ocupado por favor: ")
        
        
        locales[i][1] = input("Ingrese la ubicación del local: ")
        sep()
        locales[i][2] = input("Ingrese el rubro del local (indumentaria/perfumería/comida): ").lower()
        
        # Validación del rubro
        while locales[i][2] not in ['indumentaria', 'perfumería', 'comida']:
            locales[i][2] = input("Rubro inválido, ingrese el rubro del local nuevamente por favor: ")
        
        #se cuenta cuantas veces los rurbos fueron ingresados
        if locales[i][2] == "comida":
            comida += 1
        elif locales[i][2] == "indumentaria":
            indumentaria += 1
        elif locales[i][2] == "perfumería":
            perfumería += 1
        
        sep()
        codUsuario = input("Ingrese el código del usuario dueño del local: ")
        
        #Validación del código de usuario
        while codUsuario not in ('4','6'):
            codUsuario = input("El código de usuario no pertenece a ningún dueño, ingrese el código de nuevo por favor: ")
        
        #Ultimos elementos a insertar
        locales[i][3] = str(codLocal)
        locales[i][4] = "Activo"
        
        # Actualización del código de local para el siguiente local
        codLocal += 1
        i +=1
        
        os.system("cls")
        print("Local creado exitosamente.")
        sep()
        
        #Ordenamiento
        Ordenar()
        
        nombreLocal = input("Ingrese el nombre del local (un '0' indicará fin de la carga): ")
        os.system("cls")

#MÓDULO para modificar un local
def modificar_local():
    global locales, confirm, comida, perfumería, indumentaria, activar
    
    mostrar = input("¿Le gustaría ver los locales cargados?: ").lower()
    if mostrar in ("sí","si"):
        mostrar_locales()
    
    sep()
    confirm = input("¿Está seguro de querer modificar la información de algún local?: ").lower()
    
    if confirm in ("sí", "si"):
        sep()
        codigo = input("Ingrese el código del local que desea modificar: ")
        os.system("cls")
        
        # Buscar el local por su código
        find = True
        while find:
            
            cod = Busquedasec(3,codigo)
            
            if cod is None:
                print("Lo lamentamos pero no se encontró ningún local con ese código.")
                codigo = input("Ingrese el código del local que desea modificar de nuevo por favor: ")
            else: find = False
        
        os.system("cls")
        if locales[cod][4] == "Baja":
            activar = input("El local que desea modificar está eliminado, le gustaría restaurarlo?: ")
            if activar in ("sí","si"):
                print(f"Restaurando el local: '{locales[cod][0]}', (Código: {locales[cod][3]})")
                sep()
                locales[cod][4] == "Activo"
        else:
            print(f"Modificando el local '{locales[cod][0]}', (Código: {locales[cod][3]})")
            sep()
        #Se resta 1 a la cantidad total de locales con el rubro a modificar
        if locales[cod][2] == "comida":
            comida -= 1
        elif locales[cod][2] == "indumentaria":
            indumentaria -= 1
        elif locales[cod][2] == "perfumería":
            perfumería -= 1
        
        nombreLocal = input("Ingrese el nuevo nombre del local: ")
        os.system("cls")
        
        #Se verifica que el nombre no se esté ya usado
        find = True
        while find:
            pos = Repeticion(0,nombreLocal)
            if pos is None:
                locales[i][0] = nombreLocal
                find = False
            else:
                nombreLocal = input("El nombre del local ya existe, introduzca uno no ocupado por favor: ")
        
        locales[cod][0] = nombreLocal
        
        locales[cod][1] = input("Ingrese la nueva ubicación del local: ")
        os.system("cls")
        
        locales[cod][2] = input("Ingrese el nuevo rubro del local (indumentaria/perfumería/comida): ").lower()
        
        # Validación del rubro
        while locales[cod][2] not in ['indumentaria', 'perfumería', 'comida']:
            locales[cod][2] = input("Rubro inválido, ingrese el nuevo rubro del local nuevamente por favor: ")
        
        #Se suma 1 a la cantidad total de locales con el nuevo rubro
        if locales[cod][2] == "comida":
            comida += 1
        elif locales[cod][2] == "indumentaria":
            indumentaria += 1
        elif locales[cod][2] == "perfumería":
            perfumería += 1
        
        
        
        # Validación del código de usuario
        codUsuario = input("Ingrese el nuevo código del usuario dueño del local: ")
        while codUsuario not in ('4','6'):
            codUsuario = input("El código de usuario no pertenece a ningún dueño, ingrese el código de nuevo por favor: ")
        
        #Ordenamiento
        Ordenar()
        
        print("Local modificado exitosamente.")

#MÓDULO eliminar un local
def eliminar_local():
    global locales
    
    codigo = input("Ingrese el código del local que desea eliminar: ")
    
    # Buscar el local por su código
    find = True
    while find:
        pos = Repeticion(3,codigo)
        
        if codigo != locales[pos][3]:
            print("Lo lamentamos pero no se encontró ningún local con ese código.")
            codigo = input("Ingrese el código del local que desea modificar de nuevo por favor: ")
        else: find = False
    
    if locales[pos][4] == "Baja":
        print("Lo lamentamos pero el local que quiere eliminar ya ha sido eliminado ")
        sep()
    else:
        os.system("cls")
        print(f"Eliminando local '{locales[pos][0]}' (Código: {locales[pos][3]})")
        
        sep()
        
        confirmacion = input("¿Está seguro/a de que desea eliminar este local? (Si/No): ").lower() 
        
        if confirmacion in ("sí", "si"):
            # Cambiar el estado del local a "Baja"
            locales[pos][4] = "Baja"
            print("Local eliminado exitosamente.")
        else:
            print("Eliminación cancelada.")

#MÓDULO para mostrar los locales cargados en un mapa
def mostrar_mapa_locales():
    global locales
    
    os.system('cls')
    
    print("Mapa de Locales:")
    sep()
    
    # Crear array del mapa de locales
    fil = 10
    col = 5
    mapa_locales = [["0"] * col for _ in range(fil)]
    
    # Asignar los códigos de los locales en el mapa
    c=0
    for a in range(fil):
        for b in range(col):
            mapa_locales[a][b] = locales[c][3]
            c+=1
    
    # Mostrar el mapa de locales
    print("+" + "-" * 19 + "+")
    for fila in mapa_locales:
        print("|", end="")
        for codigo in fila:
            print(f" {codigo} ", end="|")
        print("\n+" + "-" * 19 + "+")


#MÓDULO de la sección Gestión de Locales
def menuGestionLocales():
    print(gestión_menú)
    
    sub_menu_1 = input("¿Que parte del menú de 'Gestión de Locales' le gustaría ver?: ").lower()
    os.system('cls')
    while sub_menu_1 != "e": #menú gestion de locales
        
        sep()
        if sub_menu_1 not in ("a", "b", "c", "d"):
            print("Opción inválida. Eliga una de de las opciones disponibles por favor.")
        
        elif sub_menu_1 == "a":
            sep()
            
            crear_local()
            
            calcLoc()
            sep()
        
        elif sub_menu_1 == "b": #verificación
            modificar_local()
            sep()
        
        elif sub_menu_1 == "c": 
            eliminar_local()
            sep()    
        
        else: 
            mostrar_mapa_locales()
            sep()
        
        print(gestión_menú)
        sub_menu_1 = input("¿Que parte del menú de 'Gestión de Locales' le gustaría ver?: ").lower()
    
    print("Volviendo...")
    sep()
    print(menú_Admin)
    sep()

#MÓDULO para calcular los locales de los rubros
def calcLoc():
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
    global clase_user
    clase_user = int(input("""¿Quién es usted?
    1. Administrador
    2. Dueño de local A
    3. Dueño de local B
    4. Cliente
Elija el tipo de usuario que es usted por favor: """))
    while clase_user not in (1,2,3,4):
        
        print("Opción inválida.")
        sep()
        
        clase_user = int(input("Elija el tipo de usuario que es usted por favor: "))
    os.system('cls')
    
    if clase_user == 1:
        print("¡Bienvenido Administrador/a!")
        sep()
    elif clase_user == 2:
        print("¡Bienvenido Dueño/a!")
        sep()
    elif clase_user == 3:
        print("¡Bienvenido Dueño/a!")
        sep()
    else: 
        print("¡Bienvenido Señor/a!")


def logeo():
    global intentos
    if clase_user == 1:
        while intentos != 3:   #verificación del usuario y contraseña
            login_user = input("Ingrese su nombre de usuario: ")
            login_pass = getpass.getpass("Ingrese su contraseña: ")
            
            if usuarios[0][0] == login_user   and usuarios[0][1] == login_pass: #se suman los intentos
                os.system('cls')
                print("Felicidades Administrador, has podido ingresar!")
                
                sep()
                menuPrincipal()
                
            else: 
                intentos += 1
                
                if intentos == 3: #si los intentos inválidos son 3, se cierra el programa
                    input("Lo lamentamos pero has fallado 3 veces, y debido a medidas de seguridad el programa se cerrará.")
                else:
                    print("Usuario o contraseña incorrectos. Intenta nuevamente.")
                    sep()
    
    elif clase_user == 2:
        while intentos != 3:   #verificación del usuario y contraseña
            login_user = input("Ingrese su nombre de usuario: ")
            login_pass = getpass.getpass("Ingrese su contraseña: ")
            
            if usuarios[1][0] == login_user   and usuarios[1][1] == login_pass: #se suman los intentos
                print("Felicidades Dueño A, has podido ingresar!")
                sep()
                menuDueño()
            else: 
                intentos += 1
                
                if intentos == 3: #si los intentos inválidos son 3, se cierra el programa
                    input("Lo lamentamos pero has fallado 3 veces, y debido a medidas de seguridad el programa se cerrará.")
                else:
                    print("Usuario o contraseña incorrectos. Intenta nuevamente.")
                    sep()
    elif clase_user == 3:
        while intentos != 3:   #verificación del usuario y contraseña
            login_user = input("Ingrese su nombre de usuario: ")
            login_pass = getpass.getpass("Ingrese su contraseña: ")
            
            if usuarios[2][0] == login_user   and usuarios[2][1] == login_pass: #se suman los intentos
                print("Felicidades Dueño B, has podido ingresar!")
                sep()
                menuDueño()
            else: 
                intentos += 1
                
                if intentos == 3: #si los intentos inválidos son 3, se cierra el programa
                    input("Lo lamentamos pero has fallado 3 veces, y debido a medidas de seguridad el programa se cerrará.")
                else:
                    print("Usuario o contraseña incorrectos. Intenta nuevamente.")
                    sep()
    
    else: 
        while intentos != 3:   #verificación del usuario y contraseña
            login_user = input("Ingrese su nombre de usuario: ")
            login_pass = getpass.getpass("Ingrese su contraseña: ")
            
            if usuarios[3][0] == login_user   and usuarios[3][1] == login_pass: #se suman los intentos
                print("Felicidades Cliente, has podido ingresar!")
                sep()
                menuCliente()
            
            else: 
                intentos += 1
                
                if intentos == 3: #si los intentos inválidos son 3, se cierra el programa
                    input("Lo lamentamos pero has fallado 3 veces, y debido a medidas de seguridad el programa se cerrará.")
                else:
                    print("Usuario o contraseña incorrectos. Intenta nuevamente.")
                    sep()


#PROGAMA PRINCIPAL

#bienvenida
inicio = input("Bienvenido estimado/a, ¿le interesaría ingresar al programa? (conteste con 'Si' o 'No'): ")

#se convierte al input a minúscula
respuesta = inicio.lower()

if respuesta == "si" or respuesta == "sí": #logeo
    
    usuario()
    
    logeo()
    
else: #mensaje de despedida en caso de no querer logear
    input("Entonces que tenga un buen día, hasta luego")



