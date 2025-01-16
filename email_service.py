import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente de um arquivo .env
load_dotenv()

# Função para enviar e-mail
def enviar_email(nome, email, mensagem):
    # Configurações do servidor SMTP
    servidor = os.getenv("SMTP_SERVER")
    porta = os.getenv("SMTP_PORT")
    usuario = os.getenv("SMTP_USER")
    senha = os.getenv("SMTP_PASSWORD")
    
    # Criando a mensagem
    msg = MIMEMultipart()
    msg['From'] = email
    msg['to'] = usuario
    msg['Subject'] = f"Mensagem de {nome} - {email}"

    # Corpo do e-mail
    corpo = f"Nome: {nome}\nE-mail: {email}\n\nMensagem:\n{mensagem}"
    msg.attach(MIMEText(corpo, 'plain'))

    try:
        # Conectando ao servidor SMTP
        with smtplib.SMTP_SSL(servidor, porta) as server:
            server.login(usuario, senha)
            server.sendmail(usuario, usuario, msg.as_string())  # Envia para você mesmo
        print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar o e-mail: {e}")
