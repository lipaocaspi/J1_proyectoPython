import json

def crearEntrenadores(campus : dict):
    entrenador1 = {
        "NroId" : "1",
        "Nombre" : "A",
        "Apellidos" : "A",
        "Horario" : "Dia",
        "Idrutas" : []
    }

    entrenador2 = {
        "NroId" : "2",
        "Nombre" : "A",
        "Apellidos" : "A",
        "Horario" : "Dia",
        "Idrutas" : []
    }

    entrenador3 = {
        "NroId" : "3",
        "Nombre" : "A",
        "Apellidos" : "A",
        "Horario" : "Dia",
        "Idrutas" : []
    }

    campus.get("campus").get("entrenadores").update({entrenador1["NroId"] : entrenador1})
    campus.get("campus").get("entrenadores").update({entrenador2["NroId"] : entrenador2})
    campus.get("campus").get("entrenadores").update({entrenador3["NroId"] : entrenador3})
    # print(json.dumps(campus, indent = 4))