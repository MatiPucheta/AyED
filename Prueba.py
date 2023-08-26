from os.path import getsize, exists
from pickle import load,dump
import os

AFC = 'Archivos\Clientes.dat'
AFD = 'Archivos\Dueños.dat'
AFA = 'Archivos\Admin.dat'
AFL = 'Archivos\Locales.dat'

ALC = open(AFC, 'r+b')
ALD = open(AFD, 'r+b')
ALA = open(AFA, 'r+b')
ALL = open(AFL, 'r+b')



class Cliente:
    def __init__(self, mail: str, contr: str) -> None:
        self.mail = mail
        self.contraseña = contr

class Dueño:
    def __init__(self, mail: str, contr: str) -> None:
        self.mail = mail
        self.contraseña = contr

class Admin:
    def __init__(self, mail: str, contr: str) -> None:
        self.mail = mail
        self.contraseña = contr

class Locales:
    def __init__(self, nom: str, ubi: str, rub: str,cod: int,est: str) -> None:
        self.nombre = nom
        self.ubicacion = ubi
        self.rubro = rub
        self.codigo = cod
        self.estado = est

def busSec(Alogico, dato1: str, dato2: str) -> int: #Busco tanto el mail como la contra en el archivo lógico
    tamaño = getsize(Alogico)
    Alogico.seek(0)
    encontrado = False
    while Alogico.tell() < tamaño and not encontrado:
        pos = Alogico.tell()
        vrT = load(Alogico)
        if vrT.mail == dato1 and vrT.contraseña == dato2:
            encontrado = True
    if encontrado: 
        return pos
    else:
        return -1


def busquedaDico(Afisico,Alogico, cod:int):# método de búsqueda dicotómica en base al código del local
    Alogico.seek (0, 0)
    aux =load(Alogico)
    tamReg = Alogico.tel1()
    cantReg = int(getsize(Afisico)/tamReg)
    desde = 0
    hasta = cantReg-1
    medio = (desde + hasta) // 2
    Alogico.seek(medio*tamReg, 0)
    vrEmp=load(Alogico)
    while vrEmp.codigo != cod and desde < hasta:
        if cod < vrEmp.codigo:
            hasta = medio - 1
        else:
            desde = medio + 1
        medio = (desde + hasta) // 2
        Alogico.seek(medio*tamReg, 0)
        vrEmp=load(Alogico)
    if vrEmp.codigo == cod:
        return medio*tamReg
    else:
        return -1