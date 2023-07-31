from configparser_crypt import ConfigParserCrypt
from getpass import getpass
from os.path import exists

def geratoken():
    file = 'token'
    token_data = ConfigParserCrypt()

    if exists('key') == True:
        with open('key', 'rb') as keyfile:
            aes_key = keyfile.read()
    else:
        token_data.generate_key()
        aes_key = token_data.aes_key
        with open('key', 'wb') as file_handle:
                file_handle.write(aes_key)

    token_data.add_section('login')
    token_data['login']['usuario'] = input('Nome de usuário: ')
    token_data['login']['senha'] = getpass('Senha: ')
    token_data['login']['dominio'] = input('Domínio: ')

    token_data.add_section('api')
    token_data['api']['client_id'] = input('ID do cliente da API: ')
    token_data['api']['client_secret'] = input('Segredo do cliente da API: ')

    with open(file, 'wb') as file_handle:
        token_data.write_encrypted(file_handle, aes_key=aes_key)
    print("")
    print("Novo token gerado com sucesso!")