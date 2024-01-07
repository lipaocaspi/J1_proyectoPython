import json
import funciones.corefile as cf

cf.MY_DATABASE='data/campers.json'
isEmpty = True

def verificar(valorDato, nombreDato) -> str:
    global isEmpty
    isEmpty = True
    valorDato = ""
    while (valorDato == ""):
        valorDato = input(f"{nombreDato}")
        if (valorDato != ""):
            isEmpty = False
        else:
            print(f"El dato no puede estar vacio")

def regCamper(campus : dict):
    valor = ""
    id = verificar(valor, "Ingrese ID del Camper : ")
    nombre = verificar(valor, "Ingrese nombre del Camper : ")
    apellido= verificar(valor, "Ingrese apellido del Camper : ")
    direccion = verificar(valor, "Ingrese direccion del Camper : ")
    idAcudiente = verificar(valor, "Ingrese ID del acudiente del Camper : ")
    nroTelAcudiente = verificar(valor, "Ingrese número de teléfono del acudiente del Camper :")
    nombreAcudiente = verificar(valor, "Ingrese nombre del acudiente del Camper : ")
    emailAcudiente = verificar(valor, "Ingrese email del acudiente del Camper : ")
    nroTelCel = verificar(valor, "Ingrese teléfono celular del Camper :")
    nroTelFijo = verificar(valor, "Ingrese teléfono fijo del Camper : ")
    ubicacionTelFijo = verificar(valor, "Ingrese si el teléfono pertenece a Casa o Trabajo : ")

    camper = {
        "NroId" : id,
        "Nombre" : nombre,
        "Apellido" : apellido,
        "Direccion" : direccion,
        "Acudiente" : {},
        "Telecontacto" : {},
        "Estado" : "Inscrito",
    }

    acudiente = {
        "id" : idAcudiente,
        "nrotel" : nroTelAcudiente,
        "nombre" : nombreAcudiente,
        "email" : emailAcudiente
    }

    phone = {
        "id" : str(len(phone) + 1),
        "nrotel" : "",
        "ubicacion" : ""
    }


    # camper1["Acudiente"].update({str((len(camper1["Acudiente"]) + 1)).zfill(3) : acudiente})
    # data.update({camper1["NroId"] : camper1})
    # campus.get("campus").get("campers").update(data)
    # print(json.dumps(campus, indent = 4))