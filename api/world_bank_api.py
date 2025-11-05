import requests

class WorldBankAPI:
    def __init__(self):
        self._url = "http://api.worldbank.org/v2"

    def get_eco_info (self, country_code, indicator):
        if country_code is None or indicator is None:
            return None
        
        endopoint = f'{self._url}/country/{country_code}/indicator/{indicator}'

        params = { 'format' : 'json' , 'per_page' :5  }

        try:
            response = requests.get(endopoint, params=params)

            if response.status_code == 200:
                data = response.json()
                return data
            else:
                return None
        except: 
            return None
        
    def get_countries(self):
        endpoint = f'{self._url}/country'
        params = { 'format' : 'json' , 'per_page' : 50 }
        
        try: 
            response = requests.get(endpoint, params=params)

            if response.status_code == 200:
                data = response.json()
                countries = []

                for country in data[1]:
                    if country['region'] ['value'] != 'Aggregates':
                        countries.append((country['id'], country['name']))
                return countries
            else:
                return None
        except:
            return None
    
    
    def get_indicators(self):
        indicators = {
            "SP.POP.TOTL": "Población total",
            "NY.GDP.MKTP.CD": "PIB total (US$)",
            "NY.GDP.MKTP.KD.ZG": "Crecimiento del PIB (%)",
            "NY.GDP.PCAP.CD": "PIB por persona (US$)",
            "FP.CPI.TOTL.ZG": "Inflación anual (%)",
            "SL.UEM.TOTL.ZS": "Desempleo (%)",
            "SE.SEC.NENR": "Matriculación secundaria neta (%)",
            "EG.ELC.ACCS.ZS": "Acceso a electricidad (%)",
            "SH.H2O.SMDW.ZS": "Acceso a agua potable (%)",
            "IT.NET.USER.ZS": "Usuarios de Internet (%)",
            "NE.EXP.GNFS.ZS": "Exportaciones de bienes y servicios (% del PIB)",
            "NE.IMP.GNFS.ZS": "Importaciones de bienes y servicios (% del PIB)",
        }
        return indicators
    
    def format_eco_data(self, datos):
        if datos is None or len(datos) < 2:
            return "No hay datos"
        
        texto = ""
        for item in datos[1]:  # datos[1] tiene la lista de años
            año = item['date']
            valor = item['value']

            if valor and valor > 1000:
                texto += f"{año}: US${valor:,.0f}  \n"  # 1,000,000 niños
            
            elif valor == None:
                texto += f'{año}: Dato no disponible \n'

            else:
                texto += f"{año}: {valor:.2f} %\n"

        return texto