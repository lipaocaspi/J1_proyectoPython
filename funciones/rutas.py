import os
import json

def crearRuta(campus :dict):
    data = campus.get("campus").get("rutas")
    nombre = input(f"Ingrese el nombre de la ruta : ")

    ruta = {
        "NroId" : str(len(campus["campus"]["rutas"]) + 1),
        "Nombre" : nombre,
        "Modulos" : {}
    }

    data.update({ruta["NroId"] : ruta})
    campus.get("campus").get("rutas").update(data)
    print(json.dumps(campus, indent = 4))
    os.system("pause")