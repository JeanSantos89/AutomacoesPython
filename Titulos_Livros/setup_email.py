import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# Carrega variáveis do .env
load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

print("EMAIL:", EMAIL_ADDRESS)
print("SENHA:", EMAIL_PASSWORD[:4] + "********")

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")


def config_email(para, assunto, corpo):
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = para
        msg['Subject'] = assunto
        
        msg.attach(MIMEText(corpo, 'plain'))

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.ehlo()  # inicia conversa com servidor
            server.starttls()  # ativa criptografia
            server.ehlo()  # reafirma conexão segura
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, para, msg.as_string())

        print("EMAIL ENVIADO")
    except Exception as e:
        print(f"ERRO AO ENVIAR EMAIL: {e}")


def enviar_email(destinatario, tipo_livro, TitulosLivros):
    para = destinatario
    assunto = f"Títulos dos livros - Categoria: {tipo_livro}"
    corpo = "\n".join(TitulosLivros)
    config_email(para, assunto, corpo)
