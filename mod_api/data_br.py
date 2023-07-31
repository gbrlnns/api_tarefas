import pytz
from datetime import datetime

timezone = pytz.timezone('America/Sao_Paulo')

def convertedata(data):
    data = int(round(data))/1000
    data = datetime.fromtimestamp(data, tz=timezone)
    return data.strftime("%d/%m/%Y")