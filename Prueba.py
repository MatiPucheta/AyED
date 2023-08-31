def logeo():
    global intentos
    if clase_user == 1:
        while intentos != 3:   #verificación del usuario y contraseña
            login_user = input("Ingrese su nombre de usuario: ")
            login_pass = getpass.getpass("Ingrese su contraseña: ")
            pos = busSec(login_user)
            if pos != -1:
                ALU.seek(pos)
                user = load(ALU)
                if user.claveUsuario == login_pass:
                    
            
            if usuarios[0][0] == login_user and usuarios[0][1] == login_pass: #se suman los intentos
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
            
            if usuarios[2][0] == login_user and usuarios[2][1] == login_pass: #se suman los intentos
                print("Felicidades Dueño B, has podido ingresar!")
                sep()
                menuDueño()
            else: 
                intentos += 1
                
                if intentos == 3: #si los intentos inválidos son 3, se cierra el programa
                    print("Lo lamentamos pero has fallado 3 veces, y debido a medidas de seguridad el programa se cerrará.")
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
                    print("Lo lamentamos pero has fallado 3 veces, y debido a medidas de seguridad el programa se cerrará.")
                else:
                    print("Usuario o contraseña incorrectos. Intenta nuevamente.")
                    sep()
                    
                    
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
    
def crear_local():
    global codLocal, locales, i
    global nombreLocal
    global mostrar
    global comida, indumentaria, perfumería
    
    mostrar = input("¿Le gustaría ver los locales cargados?: ").lower()
    if mostrar == 'sí' or mostrar == 'si':
        mostrar_locales()
    
    sep()
    nombreLocal = input("Ingrese el nombre del local (un '0' indicará fin de la carga): ")
    os.system("cls")
    
    while nombreLocal != '0' and codLocal != 50:
        
        print("== Crear Local ==")
        
        sep()
        
        #Se verifica que el nombre no se esté ya usado
        while Repeticion(0,nombreLocal) != -1:
            nombreLocal = input("El nombre del local ya existe, introduzca uno no ocupado por favor: ")
        locales[i][0] = nombreLocal
        
        locales[i][1] = input("Ingrese la ubicación del local: ")
        sep()
        locales[i][2] = input("Ingrese el rubro del local (indumentaria/perfumería/comida): ").lower()
        
        # Validación del rubro
        while locales[i][2] !='indumentaria' and locales[i][2] !='perfumería' and locales[i][2] !='comida':
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
        while codUsuario !='4' and codUsuario !='6':
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
