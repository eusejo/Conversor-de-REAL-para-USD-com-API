import requests
import json
import os

class Conversor():
    def __init__(self, real):
        self.resposta = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')
        self.real = real
    def converterREAL_USD(self):
        if self.resposta.status_code == 200:
            data = self.resposta.json()
            dolar_atual = float(data["USDBRL"]["high"])
            dolar = self.real / dolar_atual
            self.criar_json(data)
            return dolar
    def criar_json(self, data, file_json='arquivos/file.json'):
        if not os.path.exists('arquivos'):
            os.mkdir('arquivos')
        with open(file_json,'w',encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=True)