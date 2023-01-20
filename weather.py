import os
import json
import requests as r
from dotenv import load_dotenv
load_dotenv()
class WeatherAPI :
    
    API_KEY = os.getenv('API_KEY')
    API_URL ='http://api.weatherapi.com/v1/history.json?'

    @staticmethod
    def WeatherInformation(lat : int,long : int,date : str):
        payload = {'q': f'{lat},{long}', 'dt': f'{date}'}
        headers = {'key': f'{WeatherAPI.API_KEY}'}
        location = r.get(WeatherAPI.API_URL,params=payload,headers=headers)
        output = json.loads(location.text)
        with open('location.json','w') as file : 
            file.write(json.dumps(output,indent=4))
            file.close()
        return output

if __name__ == "__main__": 
    Weather = WeatherAPI()
    Weather_loc =Weather.WeatherInformation(48.5734053,7.7521113,'2023-01-10')
