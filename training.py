import sys
import json


def train():
    for arg in sys.argv:
        print(arg)
    dic = {
        "name": "value",
        "theta0": 9,
        "theta1": 8.2
    }

    filename = "parameters.json"

    try:
        with open(filename, 'w') as json_file:
            json.dump(dic, json_file)
        print(f"Archivo {filename} creado exitosamente.")
    except Exception as e:
        print(f"Ocurrió un error al crear el archivo {filename}: {e}")


if __name__ == "__main__":
    train()
