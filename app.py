from flask import Flask, render_template, request
from Conversor import Conversor

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        real = int(request.form['real'])
        dolar = f'{Conversor(real).converterREAL_USD():.2f}'
        return render_template('home.html', dolar=dolar)
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)