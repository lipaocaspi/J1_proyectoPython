import funciones.corefile as cf

isEmpty = True

def verificarDato(valorDato, enunciadoDato, data) -> str:
    global isEmpty
    isEmpty = True
    valorDato = ""
    while (isEmpty):
        valorDato = input(f"{enunciadoDato}")
        if (valorDato != ""):
            if (enunciadoDato == "Ingrese el ID del salón : "):
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

def regSalones(campus : dict):
    header = """
    *************************************
    *       REGISTRO DE SALONES         *
    *************************************
    """
    print(header)
    data = campus.get("campus").get("salones")
    valor = 0
    
    id = verificarDato(valor, "Ingrese el ID del salón : ", data)
    nombre = verificarDato(valor, "Ingrese el nombre del salón : ", data)

    salon = {
        "id" : id,
        "nombre" : nombre,
        "capacidad" : 0
    }

    data.update({salon["id"]: salon})
    campus.get("campus").get("salones").update(data)
    cf.UpdateFile(campus)

def buscarSalon(campus : dict) -> str:
    idSalon = input(f"Ingrese el id del salón asignado : ")
    data = campus.get("campus").get("salones").get(idSalon, -1)
    if (type(data) == dict):
        return idSalon
    else:
        print(f"No existe un salón con este código")
        return ""