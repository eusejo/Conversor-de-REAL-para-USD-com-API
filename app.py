from flask import Flask, render_template, request
from Conversor import Conversor
import json

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        real = int(request.form['real'])
        dolar = f'{Conversor(real).converterREAL_USD():.2f}'
        return render_template('home.html', dolar=dolar)
    return render_template('home.html')

@app.route('/cotacao')
def cotacao():
    with open('arquivos/file.json','r', encoding='utf-8') as file:
        json_file = json.load(file)
           
    informacoes_dolar = json.dumps(json_file, indent=4, ensure_ascii=False)
    return render_template('cotacao.html', json_file=informacoes_dolar)

if __name__ == '__main__':
    app.run(debug=True)