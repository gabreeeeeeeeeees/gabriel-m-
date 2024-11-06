#importamdo a biblioteca so Flask para fazer um si 
from flask import Flask, render_template, request,redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "chave_muito_segura"

#Criar uma lista de usário 
usuarios = {
    "admin": "admin 1234", 

}

app = Flask(__name__)

#definindo a rota principal so site
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/pagina')
def pagina():
    return render_template('pagina.html')

@app.route('/perfil')
def perfil():
    return render_template('perfil.html')

@app.route('/primeira pagina')
def primeira_pagina():
    return render_template('primeira pagina.html')



@app.route('/verificar-login', methods=['POST'])
def verificar_login():
# Pegando o que o usuário digitou no campo de entrada de user e senha
    username = request.form['username']
    password = request.form['password']

    # Verifica se o usuario digitado está na lista e se 
    # a senha está certa
    if username in usuarios and usuarios[username] == password:
        return redirect(url_for('primeira_pagina'))
    else:
    #Flash envia mensagem para o front-end
        flash('Usuário ou senha inscorretos', 'danger')
        return redirect(url_for('login'))



# parte principal do
if __name__ == '__main__':
    app.run(debug=True)