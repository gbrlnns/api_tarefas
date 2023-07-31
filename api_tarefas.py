import sys
import tkinter as tk
from tkinter import filedialog
sys.path.append('mod_api')
from mod_api.api_login import tokencheck, apilogin
from mod_api.api_excel import xlsread, xlswrite
from mod_api.api_lista import getlist
from mod_api.api_filtro import filterlist

root = tk.Tk()
root.withdraw()

filetypes = [('Pasta de Trabalho do Excel', '*.xlsx'), ('Pasta de Trabalho do Excel 97-2003', '*.xls')]

print("Abrindo seleção de arquivo...")
procxls = filedialog.askopenfilename(filetypes=filetypes)
root.destroy()
print("Arquivo selecionado: "+procxls+".")
print("")

lista_processos = xlsread(procxls)

if tokencheck() == True:
    print("Token de login localizado. Fazendo login na API do Projuris...")
    token = apilogin()
else:
    from mod_api.api_token import geratoken
    print("Token de login não encontrado. Por favor, insira os seus dados de acesso para gerar um novo.")
    print("")
    geratoken()
    print("")
    print("Fazendo login na API do Projuris...")
    token = apilogin()

proc_dict = {}
for procnum in lista_processos:
    key = "".join(procnum)
    print("")
    print("Obtendo lista de tarefas do processo nº "+key+"...")
    listatotal = getlist(procnum, token)
    if listatotal == False:
        value = "Processo não encontrado na base."
    else:
        listafiltrada = filterlist(listatotal)
        def virgulas(lista):
            if len(lista) == 0:
                return "Não há tarefas pendentes."
            else:
                start, last = lista[:-1], lista[-1]
                if start:
                    return "{} e {}".format(", ".join(start), last)
                else:
                    return last
        value = virgulas(listafiltrada)
    proc_dict.update({key:value})

print("")
print("Listas de tarefas obtidas com sucesso. Convertendo em planilha...")
planilha = filedialog.asksaveasfilename(filetypes=filetypes, defaultextension='.xlsx')
xlswrite(proc_dict, planilha)