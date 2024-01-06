import json
import funciones.corefile as cf

cf.MY_DATABASE='data/campers.json'
def NewCamper(campus : dict):
    data = campus.get("campus").get("campers")
    camper = {
        "NroId" : "",
        "Nombre" : "",
        "Apellido" : "",
        "Direccion" : "",
        "Acudiente" : {},
        "Telecontacto" : {},
        "Estado" : "",
    }

    acudiente = {
        "id" : "",
        "nrotel" : "",
        "nombre" : "",
        "email" : ""
    }

    phone = {
        "id" : "",
        "nrotel" : "",
        "ubicacion" : ""
    }


    # camper1["Acudiente"].update({str((len(camper1["Acudiente"]) + 1)).zfill(3) : acudiente})
    # data.update({camper1["NroId"] : camper1})
    # campus.get("campus").get("campers").update(data)
    # print(json.dumps(campus, indent = 4))