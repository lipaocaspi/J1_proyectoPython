import os
import json
import ui.menus as m
import funciones.salones as s

listaModulos = ["Fundamentos de programacion", "Programacion Web", "Programacion formal", "Bases de datos", "Backend"]

def crearRuta(campus : dict):
    global isIncomplete
    isIncomplete = True
    data = campus.get("campus").get("rutas")
    nombre = input(f"Ingrese el nombre de la ruta : ")
    idSalon = s.buscarSalon(campus)
    if (idSalon != ""):
        ruta = {
            "NroId" : str(len(campus["campus"]["rutas"]) + 1),
            "Nombre" : nombre,
            "modulos" : {},
            "IdSalon" : idSalon
        }
        for i, item in enumerate(listaModulos):
            modulo = {
                "Id" : str(i + 1),
                "Nombre" : item,
                "Temas" : []
            }
            print(f"")
            print(f"Módulo {item}".upper())
            print(f"")
            rta = int(input(f"¿Cuántos temas desea agregar al módulo? : "))
            j = 1
            while (j <= rta):
                tema = input(f"Ingrese el nombre del tema correspondiente al módulo : ")
                if (tema != ""):
                    modulo["Temas"].append(tema)
                    j = j + 1
                else:
                    print(f"El tema no puede estar vacio")
            ruta["modulos"].update({modulo["Id"] : modulo})
        data.update({ruta["NroId"] : ruta})
        campus.get("campus").get("rutas").update(data)
        print(json.dumps(campus, indent = 4))
        os.system("pause")
    else:
        print(f"No se puede crear una ruta sin un salón")
        os.system("pause")

def agregarCamperARuta(idCamper : str, campus : dict):
    data = campus.get("campus").get("rutas")
    if (len(data) == 0):
        print(f"No se puede agregar el camper a una ruta porque no se ha registrado ninguna ruta")
    else:
        dataC = campus.get("campus").get("campers").get(idCamper, -1)
        # dataC.update({"Ruta" : data.ruta["NroId"]})