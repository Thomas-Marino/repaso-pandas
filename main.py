# "dispositivo": "  SENSOR-01  ",    "consumo": "150",    "sector": ""
#La función debe retornar un nuevo diccionario que cumpla con las siguientes condiciones:
#- El nombre del dispositivo debe quedar sin espacios al principio ni al final.
#- El consumo debe convertirse a un número de tipo float.
#- Si el sector está vacío, debe asignarse el valor "Sin asignar".
import pandas

def limpiar_registro(registro: dict)-> dict:
    registro_df = pandas.DataFrame(registro)

    registro_df["dispositivo"] = registro_df["dispositivo"].str.strip()
    return registro_df.to_dict(orient="records")

registros = [
    {
        "dispositivo": ["  SENSOR-01  "],
        "consumo": ["150"], 
        "sector": [""]
    },
    {
        "dispositivo":["SENSOR-02  "],
        "consumo": ["90"], 
        "sector": ["SECTOR_B"]
    },
    {
        "dispositivo": ["  SENSOR-03           "],
        "consumo": ["220"], 
        "sector": ["SECTOR-A"]
    }
]    

registro_original = registros[0]
print(f"Registro original: {registro_original}")
registro_limpio = limpiar_registro(registros[0])
print(f"Registro limpio: {registro_limpio}")