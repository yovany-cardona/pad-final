import requests
import json

class Actividad1:
    def __init__(self):
        self.ruta_static = "src/pad/static/"

    def leer_api(self,url="",params={}):
        if len(parametros)==0:
            url = "{}/{}/{}/".format(url,params["coin"],params["method"])
        else:
            url = url
            
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as error:
            print(error)
            return {}
    
    def escribir_json(self,datos={},nombre_archivo="ingestion"):
        with open("{}json/{}.json".format(self.ruta_static,nombre_archivo), "w") as archivo:
            json.dump(datos,archivo)
        

    
act = Actividad1()
parametros = {"coin":"BTC","method":"ticker"}
#url = "https://www.mercadobitcoin.net/api"
url= "https://bible-api.com/data/web/random"
#datos = ingestion.obtener_datos_api(url=url, params=parametros)
datos = act.leer_api(url=url)
if len(datos)>0:
    print(json.dumps(datos,indent=4))
else:
    print("no se obtubo la consulta")
act.escribir_json(datos=datos,nombre_archivo="ingestion")