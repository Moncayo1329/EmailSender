from email.message import EmailMessage
import ssl 
import smtplib 

email_sender = 'moncayomichael23@gmail.com' 
email_password = "orar udmd idwi grws"  # fake pass !
email_receiver = 'randomtalk559@gmail.com'

subject = "Haz ejercicio, por favor" 
body = """
Todos los días puedes correr un poco. Aquí te dejo un video de motivación en YouTube: https://www.youtube.com/watch?v=oAkQ4hX17N8
"""

em = EmailMessage() 
em['From'] = email_sender 
em['To'] = email_receiver 
em['Subject'] = subject

em.set_content(body) 

context = ssl.create_default_context() 

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp: 
    smtp.login(email_sender, email_password) 
    smtp.send_message(em) 
    
