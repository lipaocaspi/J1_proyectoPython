import funciones.corefile as cf
import funciones.rutas as r

cf.MY_DATABASE='data/campus.json'
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
            elif (enunciadoDato == "Ingrese el id del trainer : "):
                dataId = data.get(valorDato, -1)
                if (type(dataId) != dict):
                    print(f"El entrenador no se encuentra registrado")
                else:
                    isEmpty = False
            elif (enunciadoDato == "Ingrese el id de la ruta : " or enunciadoDato == "Ingrese el id de la ruta asociada con el Trainer : "):
                dataId = data.get(valorDato, -1)
                if (type(dataId) != dict):
                    print(f"La ruta no se encuentra registrada")
                else:
                    isEmpty = False
            elif (enunciadoDato == "Ingrese el id del salón : "):
                dataId = data.get(valorDato, -1)
                if (type(dataId) != dict):
                    print(f"El salón no se encuentra registrado")
                else:
                    isEmpty = False
            elif (enunciadoDato == "Ingrese ID del Trainer : "):
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
    header = """
    *************************************
    *       REGISTRO DE CAMPERS         *
    *************************************
    """
    print(header)
    data = campus.get("campus").get("campers")
    valor = ""

    print(f"")
    print(f"DATOS DEL CAMPER")
    print(f"")
    id = verificarDato(valor, "Ingrese ID del Camper : ", data)
    nombre = verificarDato(valor, "Ingrese nombre del Camper : ", data)
    apellido = verificarDato(valor, "Ingrese apellidos del Camper : ", data)
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
    cf.UpdateFile(campus)

def buscarCamper(idCamper : str, campus : dict) -> dict:
    data = campus.get("campus").get("campers").get(idCamper, -1)
    if (type(data) != dict):
        print(f"No se encontró un Camper con este código")
        return {}
    else:
        return data
    
def matricularCamper(campus : dict):
    header = """
    *************************************
    *       MATRÍCULA DE CAMPERS        *
    *************************************
    """
    print(header)
    dataR = campus.get("campus").get("rutas")
    dataS = campus.get("campus").get("salones")
    id = ""

    while(id == ""):
        id = input(f"Ingrese el id del Camper que desea matricular : ")
    camper = buscarCamper(id, campus)
    
    if (camper != {} and camper["Estado"] == "Aprobado"):
        valor = 0
        r.imprimirRutas(campus)
        idRuta = verificarDato(valor, "Ingrese el id de la ruta : ", dataR)
        idSalon = dataR.get(idRuta)["IdSalon"]
        idTrainer = dataR.get(idRuta)["IdTrainer"]
        if (dataS.get(idSalon)["capacidad"] == 33):
            print(f"No se pueden agregar más Campers a esta ruta")
        else:
            fechaInicio = verificarDato(valor, "Ingrese la fecha de inicio : ", camper)
            fechaFinal = verificarDato(valor, "Ingrese la fecha final : ", camper)
            camper.update({"Estado" : "Matriculado"})
            camper.update({"idRuta" : idRuta})
            camper.update({"idSalon" : idSalon})
            camper.update({"idTrainer" : idTrainer})
            camper.update({"fechaInicio" : fechaInicio})
            camper.update({"fechaFinal" : fechaFinal})
            dataS.get(idSalon).update({"capacidad" : dataS.get(idSalon)["capacidad"] + 1})
            cf.UpdateFile(campus)
            print(f"")
            print(f"MATRICULA EXITOSA")
            print(f"")
    else:
        print(f"No se puede matricular")

def campersInscritos(campus : dict):
    data = campus.get("campus").get("campers").keys()
    if (data):
        print(f"")
        print(f"LISTADO DE CAMPERS INSCRITOS")
        print(f"")
        print("{:<15} {:<15} {:<20}".format("ID", "NOMBRE", "APELLIDO"))
        print(f"------------------------------------------------------")
        for i in list(data):
            dataC = campus.get("campus").get("campers").get(i, -1)
            if (dataC["Estado"] == "Inscrito"):
                print("{:<15} {:<15} {:<20}".format(dataC["NroId"], dataC["Nombre"], dataC["Apellido"]))
    else:
        print(f"No existen Campers con el estado inscrito")

def campersAprobados(campus : dict):
    data = campus.get("campus").get("campers").keys()
    if (data):
        print(f"")
        print(f"LISTADO DE CAMPERS APROBADOS")
        print(f"")
        print("{:<15} {:<15} {:<20}".format("ID", "NOMBRE", "APELLIDO"))
        print(f"------------------------------------------------------")
        for i in list(data):
            dataC = campus.get("campus").get("campers").get(i, -1)
            if (dataC["Estado"] == "Aprobado"):
                print("{:<15} {:<15} {:<20}".format(dataC["NroId"], dataC["Nombre"], dataC["Apellido"]))
    else:
        print(f"No existen Campers con el estado aprobado")

def campersBajoRendimiento(campus : dict):
    print(f"")
    print(f"LISTADO DE CAMPERS CON BAJO RENDIMIENTO")
    print(f"")
    print("{:<15} {:<15} {:<20}".format("ID", "NOMBRE", "APELLIDO"))
    print(f"------------------------------------------------------")
    data = campus.get("campus").get("campers").keys()
    for i in list(data):
        dataC = campus.get("campus").get("campers").get(i, -1)
        if (dataC["Estado"] == "En Riesgo"):
            print("{:<15} {:<15} {:<20}".format(dataC["NroId"], dataC["Nombre"], dataC["Apellido"]))