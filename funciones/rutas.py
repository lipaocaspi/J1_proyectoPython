import os
import json
import funciones.salones as s
import funciones.pruebas as p
import funciones.entrenadores as e
import funciones.corefile as cf

listaModulos = ["Fundamentos de programacion", "Programacion Web", "Programacion Formal", "Bases de Datos", "Backend"]

def crearRuta(campus : dict):
    global isIncomplete
    isIncomplete = True
    dataR = campus.get("campus").get("rutas")
    nombre = ""
    while(nombre == ""):
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
            valor = 0
            rta = p.verificarNota(valor, "¿Cuántos temas desea agregar al módulo? : ", int)
            j = 1
            while (j <= rta):
                tema = input(f"Ingrese el nombre del tema correspondiente al módulo : ")
                if (tema != ""):
                    modulo["Temas"].append(tema)
                    j = j + 1
                else:
                    print(f"El tema no puede estar vacio")
            ruta["modulos"].update({modulo["Id"] : modulo})
        dataR.update({ruta["NroId"] : ruta})
        campus.get("campus").get("rutas").update(dataR)
        cf.UpdateFile(campus)
        # e.asignarEntrenador(ruta, campus)
        print(json.dumps(campus, indent = 4))
    else:
        print(f"No se puede crear una ruta sin un salón")
    os.system("pause")

def buscarRuta(campus : dict) -> str:
    idRuta = ""
    while(idRuta == ""):
        idRuta = input(f"Ingrese el id de la ruta : ")
    data = campus.get("campus").get("rutas").get(idRuta, -1)
    if (type(data) == dict):
        return idRuta
    else:
        print(f"No existe una ruta con este código")
        return ""