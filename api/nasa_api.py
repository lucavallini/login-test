import requests
from datetime import datetime, timedelta
import json

class nasaApi:
    def __init__(self):
        self._api_key = "iUsyve7LjE2Hn7wrQRym68na56MKBsXHFCBvWPEY"
        self._url = "https://api.nasa.gov"

    def getApod(self, date=None): #APOD es la iamgen del dia, tomada por un satelite
        endpoint = f'{self._url}/planetary/apod' #endpoint es url q trae datos, le pasamos la url de la api y el endpoint que seria el apod
        params = {'api_key': self._api_key} #parametros para la api que es la key
        if date:
            params['date'] = date #si usuario psa una fecha, la agregamos al parametro para q busque por la fecha ingresada
        try:
            response = requests.get(endpoint, params=params) #usamos request.get para obtener datos, pasamos el endpoint y parametros
            response.raise_for_status()#si la respuesta tiene un error, lanza una excepcion
            if response.status_code == 200: #si la respuesta es 200 significa que salio bien.
                return response.json() 
            else:# en caso q no sea 200, como por ejemplo 404, seria un error, entonces retornamos un false
                return False
        except requests.exceptions.RequestException:# si hay error en pteicion, false.
            return False
    
    #obtener las fotos del rover curiosity de marte
    def getMars_photo(self, sol=None, camera=None, rover='curiosity', page= 1, earth_date = None): #sol es el dia de marte,camera es la camara del rover, rover es el nombre del rover elegido, pagina para la paginacion, earthdate es la fecha de la tierra
        endpoint = f'{self._url}/mars-photos/api/v1/rovers/{rover}/photos'
        params={'api_key': self._api_key, 'page': page}

        if sol != None: #si el usuario pasa sol, se le agrega a params
            params['sol'] = sol
        elif earth_date: #si pasa fecha terrestre, agrego a params
            params['earth_date'] = earth_date
        else: # si no hay nada, se busca el valor 1000 por default
            params['sol'] = 1000
        

        if camera: # si usario pasa camara, se agrega
            params['camera'] = camera
        
        try: 
            response = requests.get(endpoint, params=params)
            response.raise_for_status()
            if response.status_code == 200:
                return response.json()
            else:
                return False
        except requests.exceptions.RequestException:
            return False
        
    


    #asteroides q pasan cerca de la tierra, se saca con un rango de fecha
    def getNeo_list(self, start_date=None, end_date=None):
        endpoint = f'{self._url}/neo/rest/v1/feed'
        
        if not start_date:# si no hay fecha de inicio, automaticamente se pone la fecha del dia de hoy
            start_date = datetime.now().strftime('%Y-%m-%d')
        if not end_date: #si no pasa fecha de fin, retorna false, para q ponga un fecha si de fin si o si
            return False
        
        params = {'api_key': self._api_key, 'start_date': start_date, 'end_date': end_date} #pasamos parametros

        try:
            response = requests.get(endpoint, params=params)
            response.raise_for_status()
            if response.status_code == 200:
                return response.json()
            else:
                return False
        except requests.exceptions.RequestException:
            return False
    

    #para obetener la info del asteroide por id 
    def getNeo_info(self, neo_id):
        endpoint = f'{self._url}/neo/rest/v1/neo/{neo_id}'
        params = {'api_key': self._api_key}

        try:
            response = requests.get(endpoint, params=params)
            response.raise_for_status()
            if response.status_code == 200:
                return response.json()
            else:
                return False
        except requests.exceptions.RequestException:
            return False
    


    #paginacion de asteroides, es como un buscador, es una lista completa de asteroides
    def getNeo_search(self, page=0, size=20):
        endpoint = f'{self._url}/neo/rest/v1/neo/browse'
        params = {'api_key': self._api_key, 'page': page, 'size': size}

        try:
            response = requests.get(endpoint, params=params)
            response.raise_for_status()
            if response.status_code == 200:
                return response.json()
            else:
                return False
        except requests.exceptions.RequestException:
            return False