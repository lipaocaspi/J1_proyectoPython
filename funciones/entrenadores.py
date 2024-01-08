import os
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
    dataR = campus.get("campus").get("rutas")
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
        "Idrutas" : {}
    }

    dataE.update({entrenador["NroId"] : entrenador})
    campus.get("campus").get("entrenadores").update(dataE)
    IdRuta1 = c.verificarDato(valor, "Ingrese el id de la ruta Nro1 asociada con el Trainer : ", dataR)
    dataE.get(id).get("Idrutas").update({"Ruta1" : IdRuta1})
    IdRuta2 = c.verificarDato(valor, "Ingrese el id de la ruta Nro2 asociada con el Trainer : ", dataR)
    dataE.get(id).get("Idrutas").update({"Ruta2" : IdRuta2})
    cf.UpdateFile(campus)