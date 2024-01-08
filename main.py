import os
import json
import ui.menus as m
import funciones.rutas as r
import funciones.campers as c
import funciones.pruebas as p
import funciones.salones as s
import funciones.entrenadores as e

campus = {
    "campus" : {
        "campers" : {},
        "rutas" : {},
        "pruebas" : {},
        "salones" : {}, 
        "entrenadores" : {}
    }
}

if __name__ == "__main__":
    isActiveApp = True
    opMainMenu = 0
    while(isActiveApp):
        os.system("cls")
        e.crearEntrenadores(campus)
        m.mostrarMenu()
        try:
            opMainMenu = int(input(f"Ingrese una opción : "))
        except ValueError:
            print(f"Tipo de dato incorrecto")
        else:
            if (opMainMenu == 1):
                os.system("cls")
                c.regCamper(campus)
            elif (opMainMenu == 2):
                os.system("cls")
                if (len(campus.get("campus").get("salones")) == 0 and len(campus.get("campus").get("rutas")) == 0):
                    print(f"No se pueden registrar pruebas hasta que se registren salones y rutas")
                    os.system("pause")
                else:
                    id = ""
                    while(id == ""):
                        id = input(f"Ingrese el id del Camper que desea registrar la prueba : ")
                    p.regPrueba(id, campus)
            elif (opMainMenu == 3): 
                os.system("cls")
                s.regSalones(campus)
            elif (opMainMenu == 4):
                os.system("cls")
                r.crearRuta(campus)
            elif (opMainMenu == 5):
                os.system("cls")
                c.matricularCamper(campus)
            elif (opMainMenu == 6):
                pass
            elif (opMainMenu == 7):
                pass
            elif (opMainMenu == 8):
                print(f"GRACIAS POR USAR NUESTRO SERVICIO")
                isActiveApp = False
            os.system("pause")
    # c.NewCamper(campus)
    # print(json.dumps(campus, indent = 4))