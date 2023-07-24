from flask import Flask, render_template, request
import os
import yagmail

GMAIL_USERNAME = os.getenv("EMAIL_RECE")
GMAIL_SENDER = os.getenv("EMAIL_SENDER")
GMAIL_PASSWORD = os.getenv("PASSWORD_KEY")

app = Flask(__name__)
 
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    try:
        # Get the form data
        fullname = request.form['fullname']
        email = request.form['email']
        message = request.form['message']

        # Create a yagmail.SMTP object
        yag = yagmail.SMTP(GMAIL_SENDER, GMAIL_PASSWORD)

        # Compose the email
        subject = f'Contacto de {fullname}'
        msg_body = f'Nombre: {fullname}\nCorreo electrónico: {email}\nMensaje: {message}'

        yag.send(to=[GMAIL_USERNAME], subject=subject, contents=msg_body)

    except Exception as e:
       
        return render_template('contact_error.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

