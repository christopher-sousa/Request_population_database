import requests
from api_rs.api_token import request_token
import credentials

token = request_token() #Credentials using base64

def get_client_data(dataStart:str, dataEnd:str):

    if(not token["status"]):
        print(f"Token não encontrado")
        return []

    url = f"{credentials.url}/participants?limitPerPage=1000&dateStart={dataStart}&dateEnd={dataEnd}"
    headers = {'Authorization': f'Bearer {token["token"]}'}
    response = requests.get(url=url,headers=headers)
    print(response)
    if response.status_code == 200:
        data = response.json()
        return data['results']
    else:
        print(f"Falha ao obter dados dos clientes. Status code: {response.status_code}")
        return []

def get_client_data_address(id:str):

    if(not token["status"]):
        print(f"Token não encontrado")
        return []
    url = f"{credentials.url}/participants/{id}/address"
    headers = {'Authorization': f'Bearer {token["token"]}'}
    response = requests.get(url=url,headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data['results']
    else:
        print(f"Falha ao obter endereço dos clientes. Status code: {response.status_code}")
        return []
    
def get_client_data_bankaccount(id:str):

    if(not token["status"]):
        print(f"Token não encontrado")
        return []

    url = f"{credentials.url}/participants/{id}/bankaccount"
    headers = {'Authorization': f'Bearer {token["token"]}'}
    response = requests.get(url=url,headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data['results']
    else:
        print(f"Falha ao obter dados de conta bancaria dos clientes. Status code: {response.status_code}")
        return [] 
    
def get_client_data_affiliation(id:str):

    if(not token["status"]):
        print(f"Token não encontrado")
        return []

    url = f"{credentials.url}/participants/{id}/affiliation"
    headers = {'Authorization': f'Bearer {token["token"]}'}
    response = requests.get(url=url,headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Falha ao obter dados de afiliação dos clientes. Status code: {response.status_code}")
        return [] 

def get_client_social_data(id:str):

    if(not token["status"]):
        print(f"Token não encontrado")
        return []

    url = f"{credentials.url}/participants/{id}/partner"
    headers = {'Authorization': f'Bearer {token["token"]}'}
    response = requests.get(url=url,headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data['results']
    else:
        print(f"Falha ao obter dados de contato dos clientes. Status code: {response.status_code}")
        return [] 

def get_transaction_terminals(dataStart:str,dataEnd:str):

    if(not token["status"]):
        print(f"Token não encontrado")
        return []

    url = f"{credentials.url}/terminals?limitPerPage=1000&dateStart={dataStart}&dateEnd={dataEnd}"
    headers = {'Authorization': f'Bearer {token["token"]}'}
    response = requests.get(url=url,headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data['results']
    else:
        print(f"Falha ao obter dados dos terminais. Status code: {response.status_code}")
        return [] 

def get_transaction_data(dataStart:str,dataEnd:str):

    if(not token["status"]):
        print(f"Token não encontrado")
        return []

    url = f"{credentials.url}/transactions?limitPerPage=300&dateStart={dataStart}&dateEnd={dataEnd}"
    headers = {'Authorization': f'Bearer {token["token"]}'}
    response = requests.get(url=url,headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data['results']
    else:
        print(f"Falha ao obter dados das transações. Status code: {response.status_code}")
        return []