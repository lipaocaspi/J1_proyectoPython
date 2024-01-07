import os
import json
import funciones.campers as c
import funciones.pruebas as p
import ui.menus as m

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
                id = input(f"Ingrese el id del Camper que desea registrar la prueba : ")
                p.regPruebaInicial(id, campus)
            elif (opMainMenu == 3):
                pass
            elif (opMainMenu == 4):
                pass
            elif (opMainMenu == 5):
                pass
            elif (opMainMenu == 6):
                pass
            elif (opMainMenu == 7):
                pass
            elif (opMainMenu == 8):
                print(f"GRACIAS POR USAR NUESTRO SERVICIO")
                isActiveApp = False
            # os.system("pause")
    # c.NewCamper(campus)
    # print(json.dumps(campus, indent = 4))