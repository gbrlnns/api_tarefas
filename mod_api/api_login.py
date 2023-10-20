import requests
from api_token import geratoken
from os.path import exists
from configparser_crypt import ConfigParserCrypt
from time import sleep

def tokencheck():
    if exists('token'):
        return True
    else:
        return False

def apilogin():
    key = 'key'
    file = 'token'
    token_data = ConfigParserCrypt()
    with open(key, 'rb') as keyfile:
        aes_key = keyfile.read()
    token_data.aes_key = aes_key
    token_data.read_encrypted(filenames=file)
    dadoslogin = token_data['login']
    dadosapi = token_data['api']

    form = {'grant_type':'password', 'username':dadoslogin['usuario']+"$$"+dadoslogin['dominio'], 'password':dadoslogin['senha']}
    resposta = requests.post(url='https://login.projurisadv.com.br/adv-bouncer-authorization-server/oauth/token', data=form, auth=(dadosapi['client_id'], dadosapi['client_secret']))
    if resposta.status_code == 200:
        print("Login realizado com sucesso.")
        json = resposta.json()
        return json["access_token"]
    else:
        print("Falha no login. Verifique os dados e a sua conexão e tente novamente.")
        sleep(4)
        exit()