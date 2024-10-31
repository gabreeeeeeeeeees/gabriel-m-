#importamdo a biblioteca so Flask para fazer um si 
from flask import Flask, render_template, request

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


# Parte principal do programa em Phyton
if __name__=='__main__':
    app.run(debug=True)

    # VERFIFICAR O LOGIN
@app.route('/verificar-login', methods=['POST'])
def verificar_login():
# Pegando o que o usuário digitou no campo de entrada de user e senha
    username = request.form['username']
    password = request.form['password']

    # Verifica se o usuario digitado está na lista e se 
    # a senha está certa
    if username in usuarios and usuarios[username] == password:
        return f"Bem-vindo, {username}!"
    else:
        return "Usuário ou senha inválidos."






# parte principal do
if __name__ == '__main__':
    app.run(debug=True)