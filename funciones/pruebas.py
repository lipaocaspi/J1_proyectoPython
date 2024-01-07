import os
import json
import funciones.rutas as r

def verificarNota(valorDato, enunciadoDato, tipoDato) -> int:
    global isIncorrect
    isIncorrect = True
    valorDato = 0
    while (isIncorrect):
        try:
            valorDato = tipoDato(input(f"{enunciadoDato}"))
        except ValueError:
            print(f"Tipo de dato incorrecto")
        else:
            if (valorDato >= 0 and valorDato <= 100):
                isIncorrect = False
            else:
                print(f"Ingrese un valor entre 0 y 100")
    return valorDato

def regPruebaInicial(id : str, campus : dict):
    data = campus.get("campus").get("campers").get(id, -1)
    if (type(data) == dict):
        valor = 0
        if (data["Estado"] == "Inscrito"):
            notaT = verificarNota(valor, "Ingrese el valor de la nota téorica (0 a 100) : ", int)
            notaP = verificarNota(valor, "Ingrese el valor de la nota práctica (0 a 100) : ", int)
            notaTotal = (notaT + notaP) / 2
            if (notaTotal >= 60):
                estado = "Aprobado"
            else:
                estado = "Desaprobado"
            prueba = {
                "idCamper" : id,
                "nota" : notaTotal,
                "estado": estado
            }
            dataP = campus.get("campus").get("pruebas")
            dataP.update({str((len(dataP) + 1)).zfill(3) : prueba})
            campus.get("campus").get("pruebas").update(dataP)
            data.update({"Estado" : estado})
        else:
            print(f"El estado del camper no es Inscrito")
    else:
        print(f"No se encontró el id")
    
    os.system("pause")