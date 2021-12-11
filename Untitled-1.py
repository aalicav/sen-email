import smtplib
import email.message
from typing import Text
numero_emails = int(input('Quantos emails você quer enviar?'))
texto = input('Digite aqui o texto que você quer enviar:')
destinatário = str(input('Digite aqui para quem você quer enviar os emails:')).strip()
fonte = str(input('Digite aqui para quem você quer enviar os emails:')).strip()
def enviar_email(text):
    email1 = email.message.Message()
    email1['Subject'] = "Teste"
    email1['From'] = fonte
    email1['To'] = destinatário
    password = 'naotenhonada1'
    email1.add_header('Content-Type', 'text/html')
    email1.set_payload(text)
    sms = smtplib.SMTP('smtp.gmail.com: 587')
    sms.starttls()
    sms.login(email1['From'], password)
    sms.sendmail(email1['From'], [email1['To']], email1.as_string().encode('utf-8'))
    print(f'Deu certo. Enviamos "{texto}" para {destinatário}')
for c in range(0,numero_emails):
    enviar_email(texto)