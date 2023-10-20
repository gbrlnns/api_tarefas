from re import A
from data_br import convertedata

def filterlist(lista):
    listafiltrada = []
    for tarefa in lista:
        if tarefa['codigoSituacao'] == 2:
            continue
        elif tarefa['codigoSituacao'] == 3:
            continue
        elif tarefa['codigoSituacao'] == 5:
            continue
        else:
            if tarefa['descricao'] == None:
                listafiltrada.append((tarefa['nomeTarefaTipo'])+" - Fatal: "+convertedata(tarefa['dataLimite']))
            elif "Esta tarefa foi criada com base em uma intimação que você recebeu do Projuris ADV" in tarefa['descricao']:
                listafiltrada.append((tarefa['nomeTarefaTipo'])+" - Fatal: "+convertedata(tarefa['dataLimite']))
            else:
                listafiltrada.append((tarefa['nomeTarefaTipo'])+" ("+tarefa['descricao']+")"+" - Fatal: "+convertedata(tarefa['dataLimite']))
    return listafiltrada