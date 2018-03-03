from flask import Flask
from flask import render_template, redirect
app = Flask(__name__)

# rotas definem as funçoes


@app.route("/")
def index():
    return render_template('template.html')


@app.route('/botao1')
def botao():
    print('teste 1')
    return redirect('/')


@app.route('/botao2')
def botao2():
    print('teste 2')
    return redirect('/')


@app.route('/botao3')
def botao3():
    print('teste 3')
    return redirect('/')


@app.route('/botao4')
def botao4():
    print('teste 4')
    return redirect('/')


if __name__ == '__main__':
    app.run(port=8000, debug=True)
