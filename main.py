from os.path import getsize, exists
from pickle import load,dump
from datetime import datetime
import os
#Libreria escogida para mostrar codigo en rojo
from colorama import init, Fore
#librería importada para la contraseña oculta
import getpass

# Inicializa colorama
init()

#contador de filas
i = 0

F=50
C=5
# Lista para almacenar los locales
locales=[[" "]*C for i in range(F)]

# Código inicial para el primer usuario
codUsuario = 1

# Código inicial para el primer local
codLocal = 1  

#contadores de los rubros
comida = 0
indumentaria = 0
perfumería = 0

#Declaraciones de los archivos
AFU = 'Archivos\\Usuarios.dat'
AFL = 'Archivos\\Locales.dat'
AFP = 'Archivos\\Promociones.dat'
AFUP = 'Archivos\\uso_Promociones.dat'
AFN = 'Archivos\\Novedades.dat'

ALU = open(AFU, 'r+b')
ALL = open(AFL, 'r+b')
ALP = open(AFP, 'r+b')
ALUP = open(AFUP, 'r+b')
ALN = open(AFN, 'r+b')

#codUsario del usuario activo
usuarioActivo = 0

#Declaración de registros

class Usuarios:
    def __init__(self) -> None:
        self.nombreUsuario = ' '.ljust(100,' ')
        self.claveUsuario = ''.ljust(8, ' ')
        self.tipoUsuario = ''.ljust(20,' ')
        self.codUsuario = 0

class Locales:
    def __init__(self) -> None:
        self.codLocal = 0
        self.nombreLocal = ''.ljust(50,' ')
        self.ubicacionLocal = ''.ljust(50, ' ')
        self.rubroLocal = ''.ljust(50,' ')
        self.codUsuario = 0
        self.estado = ' '

class Promociones:
    def __init__(self) -> None:
        self.codPromo = 0
        self.textoPromo = ''.ljust(200,' ')
        self.fechaDesdePromo = []*3
        self.fechaHastaNevedad = []*3
        self.rubroLocal = ''.ljust(50,' ')
        self.codUsuario = 0
        self.estado = ' '

class uso_Promociones:
    def __init__(self) -> None:
        self.codCliente = 0
        self.codPromo = 0
        self.fechaUsoPromo = []*3
        

class Novedades:
    def __init__(self) -> None:
        self.codNovedad = 0
        self.textoNovedad = ''.ljust(200,' ')
        self.fechaDesdenovedad = []*3
        self.fechaHastaNevedad = []*3
        self.tipoUsuario = ''.ljust(20,' ')
        self.estado = ' '

#Variables de trabajo
user = Usuarios()
loc = Locales()
prom = Promociones()
nov = Novedades()
u_prom = uso_Promociones()

#Carga del super usuario administrador
if getsize(AFU) == 0:
    user.codUsuario = codUsuario
    user.nombreUsuario = 'admin@shopping.com'.ljust(100,' ')
    user.claveUsuario = '12345'.ljust(8, ' ')
    user.tipoUsuario = 'administrador'.ljust(20,' ')
    dump(user, ALU)
    ALU.flush()



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
    1: Crear descuentos
    2: Reporte de uso de descuentos
    3: Ver novedades
    0: Salir""")

#menú del cliente
menú_Cliente = ("""-- Menú Principal --
    1: Buscar descuentos en local
    2: Solicitar descuento
    3: Ver novedades
    0: Salir""")

#separador a fin de estética
def sep() -> None:
    return print("-"*70)

#MÓDULO del menú principal Cliente
def menuCliente() -> None:
    global intentos
    print(menú_Cliente)
    sep()
    
    elección = input("¿Qué parte del menú principal le gustaría ver?: ")
    while elección != '0':
            
        match elección:
            case '1':
                # HACER MODULO buscDescuentos()
                pass
            case '2':
                # HACER MODULO solicDescuento()
                pass
            case '3':
                print("Diagramado en Chapin.")
                pass
            case default:
                print("Opción inválida, elija nuevamente.")
                
        elección = input("¿Qué parte del menú principal le gustaría ver?: ")
    intentos = 3
    print("Que tenga un buen día, hasta luego") #mensaje de despedida


#MÓDULO del menú principal Dueño
def menuDueño() -> None:
    global intentos
    print(menú_Dueño)
    sep()
    
    elección = input("¿Qué parte del menú principal le gustaría ver?: ")
    
    while elección != '0':
        
        match elección:
            case '1':
                # HACER MODULO crearDescuentos()
                pass
            case '2':
                # HACER MODULO reportDescuentos()
                pass
            case '3':
                print("Diagramado en Chapin.")
                pass
            case default:
                print("Opción inválida, elija nuevamente.")
        
        elección = input("¿Qué parte del menú principal le gustaría ver?: ")
    intentos = 3
    print("Que tenga un buen día, hasta luego") #mensaje de despedida

#MÓDULO del menú principal Admin
def menuPrincipal() -> None:
    global intentos
    
    print(menú_Admin)
    sep()
    
    elección = int(input("¿Qué parte del menú principal le gustaría ver?: "))
    while elección != 0:
        
        if elección == 4:
            print("Diagramado en Chapin.")
        
        elif elección == 2 or elección == 3 or elección == 5:
            print("Lo lamentamos pero esta sección está en construcción")
        
        elif elección == 1:
            os.system('cls')
            sep()
            menuGestionLocales()
        
        else:
            sep()
            print("Opción inválida. Eliga una de las opciones disponibles.")
        
        sep()
        elección = int(input("¿Que parte del menú principal le gustaría ver?: "))
    intentos = 3
    print("Que tenga un buen día, hasta luego") #mensaje de despedida

#MÓDULO para mostrar los locales cargados
def mostrar_locales() -> None:
    global i
    print("== Locales Cargados ==")
    if i > 0:
        for p in range(0,i):
            print(f"Nombre: {locales[p][0]} | Ubicación: {locales[p][1]} | Rubro: {locales[p][2]} | Código: {locales[p][3]} | Estado: {locales[p][4]}")
    else:
        print("No se han cargado locales aún.")

#MÓDULO de la sección Gestión de Locales
def menuGestionLocales() -> None:
    print(gestión_menú)
    
    sub_menu_1 = input("¿Que parte del menú de 'Gestión de Locales' le gustaría ver?: ").lower()
    os.system('cls')
    while sub_menu_1 != "e": #menú gestion de locales
        
        sep()
        
        if sub_menu_1 == "a":
            sep()
            
            crear_local()
            #MODULO mostrar_rubros():
                
            calcLoc()
            sep()
        
        elif sub_menu_1 == "b": #verificación
            modificar_local()
            sep()
        
        elif sub_menu_1 == "c": 
            eliminar_local()
            sep()    
        
        elif sub_menu_1 == "d": 
            mostrar_mapa_locales()
            sep()
        
        else:
            print("Opción inválida. Eliga una de de las opciones disponibles por favor.")
        
        print(gestión_menú)
        sub_menu_1 = input("¿Que parte del menú de 'Gestión de Locales' le gustaría ver?: ").lower()
    
    print("Volviendo...")
    sep()
    print(menú_Admin)
    sep()

#MÓDULO para calcular los locales de los rubros
def calcLoc() -> None:
    global comida, indumentaria, perfumería
    
    print(f"""===Cantidad de Locales por Rubro===
        
        Rubro comida: {comida}
        Rubro indumentaria: {indumentaria}
        Rubro perfumería: {perfumería}
        """)

#MÓDULO para ordernar los locales alfabéticamente
def Ordenar() -> None:
    for a in range(0,F-1):
        for b in range(a+1,F):
            if locales[a][0] < locales[b][0]:
                for k in range(C):
                    aux = locales[a][k]
                    locales[a][k] = locales[b][k]
                    locales[b][k] = aux

#MÓDULO para buscar dicotómicamente
def Repeticion(col,dato) -> None:
    fin=i
    ini=0
    
    q = True
    while ini <= fin and q:
        mid = (ini + fin)//2
        if locales[mid][col] == dato:
            q = False
        
        elif locales[mid][col] < dato:
            fin = mid-1
        
        else:
            ini = mid+1
    #Devolución de valores
    if not q:
        return mid
    else: 
        return -1

#MÓDULO para buscar secuencialmente
def Busquedasec(col,num) -> None:
    a = 0
    while locales[a][col] != num and a <= 49:
        a += 1
    
    #Devolución de valores
    if locales[a][col] == num:
        return a
    else: 
        return -1

#MODULO para buscar secuencialmente en el archivo usuarios
def busSec(dato: str) -> int: 
    tamaño = getsize(AFU)
    ALU.seek(0)
    encontrado = False
    while ALU.tell() < tamaño and not encontrado:
        pos = ALU.tell()
        user = load(ALU)
        a = user.nombreUsuario.strip()
        if user.nombreUsuario.strip() == dato:
            encontrado = True
    if encontrado: 
        return pos
    else:
        return -1

#MODULO para buscar secuencialmente en el archivo usuarios por código
def buscSecUser(dato: int) -> int:
    tamaño = getsize(AFU)
    ALU.seek(0)
    encontrado = False
    while ALU.tell() < tamaño and not encontrado:
        pos = ALU.tell()
        vrT = load(ALU)
        if vrT.codUsuario == dato:
            encontrado = True
    if encontrado: 
        return pos
    else:
        return -1


#MODULO para buscar secuencialmente en el archivo locales por código
def buscSecCod(dato: int) -> int: 
    tamaño = getsize(AFL)
    ALL.seek(0)
    encontrado = False
    while ALL.tell() < tamaño and not encontrado:
        pos = ALL.tell()
        vrT = load(ALL)
        if vrT.codLocal == dato:
            encontrado = True
    if encontrado: 
        return pos
    else:
        return -1

#MÓDULO de busqueda dicotomica
def busquedaDico(nom:str) -> int:# método de búsqueda dicotómica
    arch = getsize(AFL)
    if arch != 0:
        ALL.seek(0)
        aux =load(ALL)
        tamReg = ALL.tell()
        cantReg = int(arch/tamReg)
        desde = 0
        hasta = cantReg-1
        medio = (desde + hasta) // 2
        ALL.seek(medio*tamReg, 0)
        vrEmp=load(ALL)
        while vrEmp.nombreLocal != nom and desde < hasta:
            if nom < vrEmp.nombreLocal:
                hasta = medio - 1
            else:
                desde = medio + 1
            medio = (desde + hasta) // 2
            ALL. seek(medio*tamReg, 0)
            vrEmp=load(ALL)
        if vrEmp.nombreLocal == nom:
            return medio*tamReg
        else:
            return -1
    return -1

#MÓDULO de ordenamiento (falso burbuja)
def OrdenarLoc() -> None: #falso burbuja
    ALL.seek(0)
    aux = load(ALL)
    tamR = ALL.tell()
    tamA = getsize(AFL)
    cantR = int(tamA/tamR)
    for i in range(cantR-1):
        for j in range(i+1, cantR):
            ALL.seek(i*tamR)
            auxi = load(ALL)
            ALL.seek(j*tamR)
            auxj = load(ALL)
            if (auxi.nombreLocal > auxj.nombreLocal):
                ALL.seek(i*tamR)  
                dump(auxj, ALL)
                ALL.seek(j*tamR)
                dump(auxi, ALL)

#MÓDULO para validar fecha
def validarFecha() -> str:
    flag = True
    while flag:
        try:
            fecha = input("Ingresa una fecha en el formato DD/MM/AAAA: ")
            datetime.strptime(fecha, '%d/%m/%Y')
            flag = False
        except ValueError:
            print("Fecha invalida")
    return fecha


def validarLong(dato: str) -> str:
    while len(dato) < 1 or len(dato) > 50:
        dato = input('No se ha cumplido con la cantidad maxima o mínima de caracteres, introduzca uno nuevamente por favor: ')
    return dato


#MÓDULO para cargar los locales
def crear_local() -> None:
    global codLocal, locales, i
    global nombreLocal
    global mostrar
    global comida, indumentaria, perfumería
    
    mostrar = input("¿Le gustaría ver los locales cargados?: ").lower()
    if mostrar == 'sí' or mostrar == 'si':
        mostrar_locales()
    
    sep()
    nombreLocal = input("Ingrese el nombre del local (un '0' indicará fin de la carga y máximo 50 caracteres): ")
    os.system("cls")
    
    #Se valida la longuitud del nombre
    nombreLocal = validarLong(nombreLocal)
    
    while nombreLocal != '0' and codLocal != 50:
        
        print("== Crear Local ==")
        
        sep()
        
        #Se verifica que el nombre no se esté ya usado
        while busquedaDico(nombreLocal) != -1:
            nombreLocal = input("El nombre del local ya existe, introduzca uno no ocupado por favor: ")
            nombreLocal = validarLong(nombreLocal)
        
        ubicacion = input("Ingrese la ubicación del local: ")
        
        rubro = input("Ingrese el rubro del local (indumentaria/perfumería/comida): ").lower()
        
        # Validación del rubro
        while rubro !='indumentaria' and rubro != 'perfumería' and rubro !='comida':
            rubro = input("Rubro inválido, ingrese el rubro del local nuevamente por favor: ")
        
        #se cuenta cuantas veces los rurbos fueron ingresados
        match rubro:
            case 'comida':
                comida += 1
            case 'indumentaria':
                indumentaria += 1
            case 'perfumería':
                perfumería += 1
        
        sep()
        codUsuario = input("Ingrese el código del usuario dueño del local: ")
        
        while buscSecUser(codUsuario) == -1:
            codUsuario = input("El código de usuario no pertenece a ningún dueño, ingrese el código de nuevo por favor: ")
        
        #Asignación de los valores
        
        loc.codLocal = codLocal
        loc.nombreLocal = nombreLocal.ljust(50, ' ')
        loc.ubicacionLocal = ubicacion.ljust(50, ' ')
        loc.rubroLocal = rubro.ljust(50, ' ')
        loc.codUsuario = codUsuario
        loc.estado = 'A'
        
        #Actualización del codigo de los locales
        codLocal+=1
        
        #Se guardan los cambios
        dump(loc,ALL)
        ALL.flush()
        
        os.system("cls")
        print("Local creado exitosamente.")
        sep()
        
        #Se ordenan los locales
        OrdenarLoc()
        
        nombreLocal = input("Ingrese el nombre del local (un '0' indicará fin de la carga y máximo 50 caracteres): ")
        
        #Agregar local al arreglo de locales
        
        os.system("cls")

#MÓDULO para modificar un local
def modificar_local() -> None:
    global comida, perfumería, indumentaria
    
    opciones = """¿Qué atributo desea modificar?

                    a. Nombre
                    b. Ubicación
                    c. Rubro
                    d. Código de usuario
                    e. Salir
                    
    Elija la opción deseada: """
    
    mostrar = input("¿Le gustaría ver los locales cargados?: ").lower()
    if mostrar == "si" or mostrar == "sí":
        mostrar_locales()
    
    sep()
    confirm = input("¿Está seguro de querer modificar la información de algún local?: ").lower()
    
    if confirm in ("sí", "si"):
        sep()
        codigo = int(input("Ingrese el código del local que desea modificar: "))
        os.system("cls")
        
        pos = buscSecCod(codigo)
        
        while pos == -1:
            print("Lo lamentamos pero no se encontró ningún local con ese código.")
            codigo = int(input("Ingrese el código del local que desea modificar de nuevo por favor: "))
            pos = buscSecCod(codigo)
        
        ALL.seek(pos)
        loc = load(ALL)
        
        os.system("cls")
        if loc.estado == "B":
            activar = input("El local que desea modificar está eliminado, le gustaría restaurarlo?: ").lower
            if activar == "sí" or activar == "si":
                sep()
                print(f"Restaurando el local: '{loc.nombreLocal.strip()}', (Código: {loc.codLocal})")
                sep()
                loc.estado = "A"
        else:
            print(f"Modificando el local '{loc.nombreLocal.strip()}', (Código: {loc.codLocal})")
            sep()
        
        rta = input(opciones)
        
        while rta != "e":
            os.system('cls')
            match rta:
                
                case 'a':
                    nomLocal = input("Ingrese el nuevo nombre del local (máximo 50 caracteres): ")
                    
                    #Se valida la longuitud del nombre
                    nombreLocal = validarLong(nomLocal)
                    
                    while busquedaDico(nombreLocal) != -1:
                        nombreLocal = input("El nombre del local ya existe, introduzca uno no ocupado por favor: ")
                        nombreLocal = validarLong(nomLocal)
                    
                    loc.nombreLocal = nomLocal.ljust(50,' ')
                    
                    os.system('cls')
                    
                    print("Nombre modificado con éxito.")
                
                case 'b':   
                    ubi = input("Ingrese la nueva ubicación del local: ")
                    
                    loc.ubicacionLocal = ubi.ljust(50,' ')
                    
                    os.system('cls')                
                    print("Ubicación modificada con éxito.")
                
                case 'c':
                    #Se resta 1 a la cantidad total de locales con el rubro a modificar
                    match loc.rubroLocal.strip():
                        case 'comida':
                            comida -= 1
                        case 'indumentaria':
                            indumentaria -= 1
                        case 'perfumería':
                            perfumería -= 1        
                    
                    rubro = input("Ingrese el nuevo rubro del local (indumentaria/perfumería/comida): ").lower()
                    
                    while rubro !='indumentaria' and rubro != 'perfumería' and rubro !='comida':
                        rubro = input("Rubro inválido, ingrese el rubro del local nuevamente por favor: ")
                    
                    match rubro:
                        case 'comida':
                            comida += 1
                        case 'indumentaria':
                            indumentaria += 1
                        case 'perfumería':
                            perfumería += 1
                    
                    
                    loc.rubroLocal = rubro.ljust(50,' ')
                    
                    os.system('cls')                
                    print("Rubro modificado con éxito.")
                
                case 'd':
                    codUser = int(input("Ingrese el nuevo código del usuario dueño del local: "))
                    
                    while buscSecUser(codUser) == -1:
                        codUser = int(input("El código de usuario no pertenece a ningún dueño, ingrese el código de nuevo por favor: "))
                    
                    loc.codUsuario = codUser
                    
                    os.system('cls')
                    print("Código de usuario modificado con éxito.")
                
                case 'e':
                    pass
                
                case default:
                    print('Opción inválida')
            
            rta = input(opciones)
        
        os.system('cls')
        
        ALL.seek(pos)
        dump(loc, ALL)
        ALL.flush()
        
        os.system('cls')
        
        print("Local modificado exitosamente.")
        
        #Ordenamiento
        OrdenarLoc()
        
        os.system('cls')
        
#MÓDULO eliminar un local
def eliminar_local() -> None:   
    global comida, perfumería, indumentaria
    
    mostrar = input("¿Le gustaría ver los locales cargados?: ").lower()
    if mostrar == "si" or mostrar == "sí":
        mostrar_locales()
    sep()
    codigo = input("Ingrese el código del local que desea eliminar: ")
    
    pos = buscSecCod(codigo)
    
    while pos == -1:
        print("Lo lamentamos pero no se encontró ningún local con ese código.")
        codigo = input("Ingrese el código del local que desea modificar de nuevo por favor: ")
        pos = buscSecCod(codigo)

    ALL.seek(pos)
    loc = load(ALL)
    
    if loc.estado == "B":
        print("Lo lamentamos pero el local que quiere eliminar ya ha sido eliminado.")
        sep()
    else:
        os.system("cls")
        print(f"Eliminando local '{loc.nombreLocal}' (Código: {loc.codLocal})")
        
        sep()
        
        confirmacion = input("¿Está seguro/a de que desea eliminar este local? (Si/No): ").lower() 
        
        if confirmacion == 'sí' or confirmacion == 'si':
            
            match loc.rubroLocal:
                case 'comida':
                    comida -= 1
                case 'indumentaria':
                    indumentaria -= 1
                case 'perfumería':
                    perfumería -= 1
                
            # Cambiar el estado del local a "Baja"
            loc.estado = "B"
            dump(loc,ALL)
            ALL.flush()
            print("Local eliminado exitosamente.")
        else:
            print("Eliminación cancelada.")

#MÓDULO para mostrar los locales cargados en un mapa
def mostrar_mapa_locales() -> None:
    arch = getsize(AFL)
    if arch != 0:
        ALL.seek(0)
        aux =load(ALL)
        tamReg = ALL.tell()
        cantReg = int(arch/tamReg)
        os.system('cls')
        
        print("Mapa de Locales:")
        sep()
        
        # Crear array del mapa de locales
        fil = 10
        col = 5
        mapa_locales = [[0] * col for _ in range(fil)]
        
        ALL.seek(0)
        a = 0
        while ALL.tell() < arch and a < fil:
            b = 0
            while ALL.tell < arch and b < col:
                loc = load(ALL)
                if loc.estado == 'B':
                    mapa_locales[a][b] = -loc.codLocal
                else:
                    mapa_locales[a][b] = loc.codLocal
                b+=1
            a += 1
        
        # Mostrar el mapa de locales
        print('+' + '-' * 29 + '+')
        for fila in mapa_locales:
            print('|', end='')
            for codigo in fila:
                if codigo < 0:
                    
                    if -codigo > 9:
                        print(Fore.RED + f' {-codigo}  ' + Fore.RESET, end='|')
                    else:
                        print(Fore.RED + f'  {-codigo}  ' + Fore.RESET, end='|')
                
                elif codigo > 9:
                    print(f' {codigo}  ', end='|')
                
                else:
                    print(f'  {codigo}  ', end='|')
            
            
            print('\n+' + '-' * 29 + '+')
            
            if mapa_locales[fil-1][col] != 0:
                print('\nPróximamente se habilitará un mapa con los demás locales...')
    else:
        print('No hay locales cargados. Por ende no se encuetra habilitado el mapa de locales')

#MÓDULO de logeo de los usuarios
def Logeo() -> None:
    global intentos
    global usuarioActivo
    while intentos != 3:   #verificación del usuario y contraseña
        nom = input("Ingrese su nombre de usuario: ")
        
        contra = getpass.getpass("Ingrese su contraseña: ")
        
        pos = busSec(nom)
        if pos != -1:
            ALU.seek(pos)
            user = load(ALU)
            if user.claveUsuario.strip() == contra:
                usuarioActivo = user.codUsuario
                match (user.tipoUsuario.strip()):
                    case 'cliente':
                        os.system('cls')
                        menuCliente()
                    case 'dueño':
                        os.system('cls')
                        menuDueño()
                    case 'administrador':
                        os.system('cls')
                        menuPrincipal()
            else:
                os.system('cls')
                print('Clave de usuario incorrecta')
        else:
            os.system('cls')
            print('Usuario no existente')
        intentos += 1

#MÓDULO de registro de usuarios
def Registro() -> None:
    global codUsuario
    ALU.seek(0)
    aux = load(ALU)
    tamañoR = ALU.tell()
    cantR = getsize(AFU)//tamañoR
    ultimoR = cantR*tamañoR
    ALU.seek(ultimoR)
    codUsuario+=1
    nom = input("Bienvenido seas, ingrese su nombre de usuario para registrarse por favor (un '0' indica anulación del procedimiento y máximo 100 caracteres): ")
    
    while busSec(nom) != -1 and nom != '0':
        nom = input('Lamentamos comunicarle el nombre ya esta siendo utilizado. Ingrese uno diferente por favor (máximo 100 caracteres): ')
    
    while len(nom) < 1 and len(nom) > 100:
        nom = input('Longitud del nombre no válida, máximo 100 caracteres: ')
    if nom != '0':
        contra = getpass.getpass("Ingrese su contraseña por favor (máximo 8 caracteres): ")
        
        while len(contra) < 1 and len(contra) > 8:
            nom = input('Longuitud del nombre no válida, máximo 8 caracteres: ')
        
        cliente = load(ALU)
        cliente.codUsuario = codUsuario,
        cliente.nombreUsuario = nom.ljust(100, ' '),
        cliente.claveUsuario = contra.ljust(8, ' '),
        cliente.tipoUsuario = 'cliente'.ljust(20, ' ')
        dump(cliente,ALU)
        ALU.flush()
        os.system('cls')
        print('¡¡Has podido registrarte exitosamente!!\n')

#MÓDULO de verificación del tipo de usuario

def Inicio() -> None:
    menu = """Eliga la opción que desee

    1. Ingresar con usuario registrado
    
    2. Registrarse como cliente
    
    3. Salir
    
    Elija una opción:
"""

    opcion = input(menu)
    while opcion != '3':
        sep()
        
        match opcion:
            case '1':
                Logeo()
            case '2':
                Registro()
            case '3':
                pass
            case default:
                print('Opción invalida, eliga nueva de nuevo')
        sep()
        opcion = input(menu)

#PROGAMA PRINCIPAL

#bienvenida
inicio = input("Bienvenido estimado/a, ¿le interesaría ingresar al programa? (conteste con 'Si' o 'No'): ")

#se convierte al input a minúscula
respuesta = inicio.lower()

if respuesta == "si" or respuesta == "sí": #logeo
    
    Inicio()
    
else: #mensaje de despedida en caso de no querer logear
    print("Que tenga un buen día, hasta luego")

#Cierre de archivos
ALU.close()
ALL.close()
ALP.close()
ALUP.close()
ALN.close()


