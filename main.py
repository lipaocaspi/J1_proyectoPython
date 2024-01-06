import json
import funciones.campers as c

campus = {
    "campus" : {
        "campers" : {},
        "rutas" : {},
        "pruebas" : {},
        "salones" : {}
    }
}

if __name__ == "__main__":
    c.NewCamper(campus)
    # print(json.dumps(campus, indent = 4))