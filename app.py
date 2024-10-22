#importamdo a biblioteca so Flask para fazer um si 
from flask import Flask, render_template, request

app = Flask(__name__)

#definindo a rota principal so site
@app.router('/')
def home():
    return render_template('index.html')

# Parte principal do programa em Phyton
if __name__=='__main__':
    app.run(debug=True)