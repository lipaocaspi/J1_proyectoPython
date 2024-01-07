import os
import json
import funciones.corefile as cf

cf.MY_DATABASE='data/campers.json'
isEmpty = True

def verificarDato(valorDato, enunciadoDato, data) -> str:
    global isEmpty
    isEmpty = True
    valorDato = ""
    while (isEmpty):
        valorDato = input(f"{enunciadoDato}")
        if (valorDato != ""):
            if (enunciadoDato == "Ingrese ID del Camper : "):
                dataId = data.get(valorDato, -1)
                if (type(dataId) == dict):
                    print(f"El ID ya se encuentra registrado")
                else:
                    isEmpty = False
            else:
                isEmpty = False
        else:
            print(f"El dato no puede estar vacio")
    return valorDato
    
def regCamper(campus : dict):
    data = campus.get("campus").get("campers")
    valor = ""
    print(f"")
    print(f"DATOS DEL CAMPER")
    print(f"")
    id = verificarDato(valor, "Ingrese ID del Camper : ", data)
    nombre = verificarDato(valor, "Ingrese nombre del Camper : ", data)
    apellido= verificarDato(valor, "Ingrese apellidos del Camper : ", data)
    direccion = verificarDato(valor, "Ingrese direccion del Camper : ", data)
    nroTelCel = verificarDato(valor, "Ingrese teléfono celular del Camper : ", data)
    nroTelFijo = verificarDato(valor, "Ingrese teléfono fijo del Camper : ", data)
    ubicacionTelFijo = verificarDato(valor, "Ingrese si el teléfono pertenece a Casa o Trabajo : ", data)
    print(f"")
    print(f"DATOS DEL ACUDIENTE")
    print(f"")
    idAcudiente = verificarDato(valor, "Ingrese ID del acudiente del Camper : ", data)
    nroTelAcudiente = verificarDato(valor, "Ingrese número de teléfono del acudiente del Camper : ", data)
    nombreAcudiente = verificarDato(valor, "Ingrese nombre del acudiente del Camper : ", data)
    emailAcudiente = verificarDato(valor, "Ingrese email del acudiente del Camper : ", data)

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

    phoneCel = {
        "id" : str((len(camper["Telecontacto"]) + 1)),
        "nrotel" : nroTelCel,
        "ubicacion" : ""
    }

    phoneFijo = {
        "id" : str((len(camper["Telecontacto"]) + 1)),
        "nrotel" : nroTelFijo,
        "ubicacion" : ubicacionTelFijo
    }

    camper["Acudiente"].update({str((len(camper["Acudiente"]) + 1)).zfill(3) : acudiente})
    camper["Telecontacto"].update({str((len(camper["Telecontacto"]) + 1)).zfill(3) : phoneCel})
    camper["Telecontacto"].update({str((len(camper["Telecontacto"]) + 1)).zfill(3) : phoneFijo})
    data.update({camper["NroId"] : camper})
    campus.get("campus").get("campers").update(data)
    # print(json.dumps(campus, indent = 4))
    os.system("pause")