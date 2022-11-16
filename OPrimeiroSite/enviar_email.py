import smtplib
import email.message


def send_email(corpo, nome, oemail, telefone):
    corpo_email = f"""<p><strong>Nome: {nome}</strong></p>
    <p><strong>Email: {oemail}</strong></p>
    <p><strong>Telefone: {telefone}</strong></p>
    <strong>Mensagem:</strong> {corpo}"""

    msg = email.message.Message()
    msg['Subject'] = "Cliente do site"
    msg['From'] = 'luizgamerbr047@gmail.com'
    msg['To'] = 'luizgamerbr047@gmail.com'
    password = 'dqkjtiaskgjrmizb'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))







