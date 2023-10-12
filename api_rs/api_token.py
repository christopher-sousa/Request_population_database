import requests
import credentials
from processing import encoded_base64 as b64 
key = b64.encoded() #Credentials using base64

# Request token access
def request_token():
    
    url = f"{credentials.url}/accessToken"
    headers = {'Authorization': f'Basic {key}'}
    response = requests.post(url=url,headers=headers)

    if response.status_code == 200:
        data = response.json()
        return {"status": True, "token": data['token']}
    else:
        print(f"Falha ao obter dados dos clientes. Status code: {response.status_code}")
        return {"status": True, "token": ''}