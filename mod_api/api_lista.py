import requests
from time import sleep


def getlist(processo, token):
    headers = {'Content-Type': 'application/json', 'accept': 'application/json', 'Authorization': 'Bearer '+token}
    proc_json = {'numeroProcesso': str(processo)}
    resposta = requests.post('https://api.projurisadv.com.br/adv-service/tarefa/consulta-com-paginacao', headers=headers, json=proc_json)
    if resposta.status_code == 204:
        return False
    elif resposta.status_code == 200:
        resposta_json = resposta.json()
        return resposta_json["tarefaConsultaWs"]
    else:
        procfalha = "".join(processo)
        print("Falha ao obter a lista de tarefas do processo nº "+procfalha+". Tente novamente mais tarde.")
        sleep(4)
        exit()