from flask import Flask, render_template, request, url_for, redirect
from email_service import enviar_email

app = Flask(__name__)

# Rota principal (home page)
@app.route('/')
def home():
    return render_template('index.html')



@app.route('/contact', methods=['POST'])
def contato():
    nome = request.form['name']
    email = request.form['email']
    mensagem = request.form['message']
    
    # Enviar e-mail
    enviar_email(nome, email, mensagem)
    
    # Redirecionar para uma página de agradecimento ou de confirmação
    return redirect(url_for('home'))



if __name__ == '__main__':
    app.run(debug=True)