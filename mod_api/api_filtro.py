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
            listafiltrada.append((tarefa['nomeTarefaTipo'])+" - Fatal: "+convertedata(tarefa['dataLimite']))
    return listafiltrada