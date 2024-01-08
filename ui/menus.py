import os
import main as m
import funciones.campers as c

menuP = ["Registrar Camper", "Registrar Prueba", "Registro Áreas de Entrenamiento", "Creación Rutas de Entrenamiento", "Gestor de Matriculas", "Modulo de Reportes", "Salir"]
menuReporte = ["Campers Inscritos", "Campers Matriculados", "Entrenadores de Campus", "Campers con bajo rendimiento", "Buscar Ruta de Entrenamiento", "Resumen de Módulos", "Volver"]

def mostrarMenu():
    c.cf.checkFile(m.campus)
    header = """
    *************************************
    * SEGUIMIENTO ACADÉMICO CAMPUSLANDS *
    *************************************
    """
    print(header)
    for i, item in enumerate(menuP):
        print(f"{i+1} - {item}")

def mostrarMenuR():
    header = """
    *************************************
    *        MÓDULO DE REPORTES         *
    *************************************
    """
    print(header)
    for i, item in enumerate(menuReporte):
        print(f"{i+1} - {item}")

    isIncorrect = True
    opMenu = 0
    while(isIncorrect):
        try:
            opMenu = int(input(f"Ingrese una opción : "))
        except ValueError:
            print(f"Tipo de dato incorrecto")
        else:
            if (opMenu == 1):
                os.system("cls")
            elif (opMenu == 2):
                os.system("cls")
            elif (opMenu == 3): 
                os.system("cls")
            elif (opMenu == 4):
                os.system("cls")
            elif (opMenu == 5):
                os.system("cls")
            elif (opMenu == 6):
                os.system("cls")
            elif (opMenu == 7):
                isIncorrect = False