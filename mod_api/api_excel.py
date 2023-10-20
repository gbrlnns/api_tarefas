import pandas as pd


def xlsread(file):
    processos = pd.read_excel(file, usecols='A')
    return processos.values.tolist()


def xlswrite(dict, file):
    dataframe = pd.DataFrame.from_dict(dict, orient='index', columns=["Tarefas pendentes"])
    dataframe.to_excel(file)