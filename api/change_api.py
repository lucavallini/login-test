import requests
from datetime import datetime, timedelta

class ChangeAPi:
    def __init__(self):
        self.url = "https://v6.exchangerate-api.com/v6/"
        self.api_key= "f602a7d2eff20ba66b6f2953"
    
    def get_rate(self, moneda, cambio):
        try:
            response = requests.get(f'{self.url}{self.api_key}/latest/{moneda}')
            if response.status_code == 200:
                datos = response.json()
                tasa = datos['conversion_rates'][cambio]
                return tasa
            return None
        except:
            return None
    

    def get_monedas(self):
        total_monedas = {
            "USD": "Dólar Estadounidense",
            "EUR": "Euro",
            "ARS": "Peso Argentino",
            "BRL": "Real Brasileño",
            "MXN": "Peso Mexicano", 
            "GBP": "Libra Esterlina",
            "JPY": "Yen Japonés",
            "CNY": "Yuan Chino",
            "CAD": "Dólar Canadiense",
            "AUD": "Dólar Australiano",
            "CHF": "Franco Suizo",
            "RUB": "Rublo Ruso",
            "INR": "Rupia India",
            "TRY": "Lira Turca",
            "KRW": "Won Surcoreano",
            "IDR": "Rupia Indonesia",
            "ZAR": "Rand Sudafricano",
            "NZD": "Dólar Neozelandés",
            "HKD": "Dólar Hongkonés",
            "SGD": "Dólar Singapurense",
            "SEK": "Corona Sueca",
            "NOK": "Corona Noruega",
            "DKK": "Corona Danesa",
            "PLN": "Zloty Polaco",
            "THB": "Baht Tailandés",
            "HUF": "Florín Húngaro",
            "CZK": "Corona Checa",
            "CLP": "Peso Chileno",
            "PEN": "Sol Peruano",
            "COP": "Peso Colombiano"
        }
        return total_monedas