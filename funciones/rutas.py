import funciones.salones as s
import funciones.pruebas as p
import funciones.campers as c
import funciones.corefile as cf

listaModulos = ["Fundamentos de programacion", "Programacion Web", "Programacion Formal", "Bases de Datos", "Backend"]

def crearRuta(campus : dict):
    header = """
    *************************************
    *        CREACIÓN DE RUTAS          *
    *************************************
    """
    print(header)
    global isIncomplete
    isIncomplete = True
    dataR = campus.get("campus").get("rutas")
    dataE = campus.get("campus").get("entrenadores")
    nombre = ""
    valor = 0
    
    while(nombre == ""):
        nombre = input(f"Ingrese el nombre de la ruta : ")
    idSalon = s.buscarSalon(campus)
    if (idSalon != ""):
        idTrainer = c.verificarDato(valor, "Ingrese el id del trainer : ", dataE)
        if (dataE.get(idTrainer)["RutasAsignadas"] < 2):
            ruta = {
                "NroId" : str(len(campus["campus"]["rutas"]) + 1),
                "Nombre" : nombre,
                "modulos" : {},
                "IdSalon" : idSalon,
                "IdTrainer" : idTrainer
            }
            for i, item in enumerate(listaModulos):
                modulo = {
                    "Id" : str(i + 1),
                    "Nombre" : item,
                    "Temas" : []
                }
                print(f"")
                print(f"Módulo {item}".upper())
                print(f"")
                valor = 0
                rta = 2
                j = 1
                while (j <= rta):
                    tema = input(f"Ingrese el nombre del tema correspondiente al módulo : ")
                    if (tema != ""):
                        modulo["Temas"].append(tema)
                        j = j + 1
                    else:
                        print(f"El tema no puede estar vacio")
                ruta["modulos"].update({modulo["Id"] : modulo})
            dataR.update({ruta["NroId"] : ruta})
            dataE.get(idTrainer).update({"RutasAsignadas" : dataE.get(idTrainer)["RutasAsignadas"] + 1})
            campus.get("campus").get("rutas").update(dataR)
            campus.get("campus").get("entrenadores").update(dataE)
            cf.UpdateFile(campus)
        else:
            print(f"No se le pueden asignar más rutas a este Trainer")
    else:
        print(f"No se puede crear una ruta sin un salón")

def buscarRuta(campus : dict) -> str:
    idRuta = ""
    while(idRuta == ""):
        idRuta = input(f"Ingrese el id de la ruta : ")
    data = campus.get("campus").get("rutas").get(idRuta, -1)
    if (type(data) == dict):
        return idRuta
    else:
        print(f"No existe una ruta con este código")
        return ""
    
def mostrarRuta(idRuta : str, campus : dict):
    print(f"")
    print(f"RUTA")
    print(f"")
    dataR = campus.get("campus").get("rutas").get(idRuta, -1)
    dataC = campus.get("campus").get("campers").keys()
    dataE = campus.get("campus").get("entrenadores").get(dataR["IdTrainer"], -1)
    print(f"\tCAMPERS")
    print("{:<15} {:<15} {:<20}".format("ID", "NOMBRE", "APELLIDO"))
    for i in list(dataC):
        data = campus.get("campus").get("campers").get(i, -1)
        if (("idRuta" in data) and data["idRuta"] == idRuta):
            print("{:<15} {:<15} {:<20}".format(data["NroId"], data["Nombre"], data["Apellido"]))
    print(f"")
    print(f"\tENTRENADOR")
    print("{:<15} {:<15} {:<20}".format("ID", "NOMBRE", "APELLIDO"))
    print("{:<15} {:<15} {:<20}".format(dataE["NroId"], dataE["Nombre"], dataE["Apellidos"]))

def imprimirRutas(campus : dict):
    dataR = campus.get("campus").get("rutas").keys()
    print(f"")
    print("{:<15} {:<15}".format("ID", "NOMBRE RUTA"))
    print(f"")
    for i in list(dataR):
        data = campus.get("campus").get("rutas").get(i, -1)
        print("{:<15} {:<15}".format(data["NroId"], data["Nombre"]))
