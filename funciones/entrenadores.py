import funciones.campers as c
import funciones.corefile as cf

def regEntrenadores(campus : dict):
    header = """
    *************************************
    *     REGISTRO DE ENTRENADORES      *
    *************************************
    """
    print(header)
    dataE = campus.get("campus").get("entrenadores")
    valor = ""
    
    id = c.verificarDato(valor, "Ingrese ID del Trainer : ", dataE)
    nombre = c.verificarDato(valor, "Ingrese nombre del Trainer : ", dataE)
    apellido = c.verificarDato(valor, "Ingrese apellidos del Trainer : ", dataE)
    horario = c.verificarDato(valor, "Ingrese horario del Trainer (Dia o Tarde) : ", dataE)
    
    entrenador = {
        "NroId" : id,
        "Nombre" : nombre,
        "Apellidos" : apellido,
        "Horario" : horario,
        "RutasAsignadas" : 0
    }

    dataE.update({entrenador["NroId"] : entrenador})
    campus.get("campus").get("entrenadores").update(dataE)
    cf.UpdateFile(campus)

def entrenadoresCampus(campus : dict):
    print(f"")
    print(f"LISTADO DE ENTRENADORES")
    print(f"")
    print("{:<15} {:<15} {:<20}".format("ID", "NOMBRE", "APELLIDO"))
    print(f"------------------------------------------------------")
    data = campus.get("campus").get("entrenadores").keys()
    for i in list(data):
        dataE = campus.get("campus").get("entrenadores").get(i, -1)
        print("{:<15} {:<15} {:<20}".format(dataE["NroId"], dataE["Nombre"], dataE["Apellidos"]))