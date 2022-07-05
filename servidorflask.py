# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 12:28:58 2022

@author: Daniel
"""

# save this as app.py
# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
from flask import Flask
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from flask  import request
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/email")
def enviarCorreo():
    hashString = request.args.get("hash")
    if(hashString == os.environ.get('SECURITY_HASH')):  
        
        destino = request.args.get("correo_destino")
        
        asunto = request.args.get("asunto")
        
        mensaje  = request.args.get("mensaje")
        
        message = Mail(
            from_email ='danielzuluaga106@gmail.com',
            to_emails = destino,
            subject = asunto,
            html_content = mensaje)
        try:
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(message)
            print("mensaje enviado")
            return "ok"
        except Exception as e:
            print(e.message)
            return "ko"
    else:
        print("Sin Hash")
        return "has error"

if __name__ == "__main__":
    app.run()