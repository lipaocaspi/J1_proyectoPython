import funciones.corefile as cf

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
            if (int(valorDato) >= 0 and int(valorDato) <= 100):
                isIncorrect = False
            elif (tipoDato == str and valorDato == ""):
                print(f"El dato no debe estar vacio")
            else:
                print(f"Ingrese un valor entre 0 y 100")
    return valorDato

def regPrueba(id : str, campus : dict):
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
            cf.UpdateFile(campus)
        elif (data["Estado"] == "Matriculado"):
            idModulo = ""
            while (idModulo not in ["1", "2", "3", "4", "5"]):
                idModulo = verificarNota(valor, "Ingrese el id del módulo cuyas pruebas quiere registrar : ", str)
            notaT = verificarNota(valor, "Ingrese el valor de la nota téorica (0 a 100) : ", int)
            notaP = verificarNota(valor, "Ingrese el valor de la nota práctica (0 a 100) : ", int)
            notaQT = verificarNota(valor, "Ingrese el valor de la nota de quices y trabajos (0 a 100) : ", int)
            notaTotal = (notaT * 0.3) + (notaP *0.6) + (notaQT * 0.1)
            if (notaTotal >= 60):
                estado = "Matriculado"
            else:
                estado = "En Riesgo"
            prueba = {
                "idCamper" : id,
                "idModulo": idModulo,
                "nota" : notaTotal,
                "estado": estado
            }
            dataP = campus.get("campus").get("pruebas")
            dataP.update({str((len(dataP) + 1)).zfill(3) : prueba})
            campus.get("campus").get("pruebas").update(dataP)
            data.update({"Estado" : estado})
            cf.UpdateFile(campus)
        else:
            print(f"El estado del Camper no es Matriculado")
    else:
        print(f"No se encontró el id")