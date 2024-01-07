import os

menuP = ["Registrar Camper", "Registrar Prueba", "Registro Áreas de Entrenamiento", "Creación Rutas de Entrenamiento", "Gestor de Matriculas", "Consulta de Estudiantes en Riesgo", "Modulo de Reportes", "Salir"]

def mostrarMenu():
    header = """
    *************************************
    * SEGUIMIENTO ACADÉMICO CAMPUSLANDS *
    *************************************
    """
    print(header)
    for i, item in enumerate(menuP):
        print(f"{i+1} - {item}")