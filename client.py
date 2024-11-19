import json
import requests  # type: ignore

class Client(object):
    def __init__(self, url: str, ssl_verify: bool = True, cert_path: str = None):
        self.url = url
        if cert_path:
            self.ssl_verify = cert_path
        else:
            self.ssl_verify = ssl_verify

    def get(self) -> dict:
        try:
            response = requests.get(self.url, verify=self.ssl_verify)
            response.raise_for_status()
            body = response.content
            return json.loads(body)
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return []
        
if __name__ == '__main__':
    URL = 'https://api.met.no/weatherapi/airqualityforecast/0.1/stations'
    client = Client(URL)
    stations = client.get()
    if stations:
        print('Name of the first station (alphabetically) = ' + stations[0].get('name'))
    else:
        print('No stations found.')
    client = Client('https://api.met.no/weatherapi/airqualityforecast/0.1/stations')
    stations = client.get()
