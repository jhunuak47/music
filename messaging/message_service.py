# message_service.py
import smtplib
from email.message import EmailMessage

def send_message(recipient, subject, body):
    sender_email = "jhunu1201@gmail.com"  
    sender_password = "ouhtqnbzrozynazt" 

    message = EmailMessage()
    message.set_content(body)
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = recipient

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)  
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(message)
        print("Message sent successfully")
    except smtplib.SMTPException as e:
        print(f"An error occurred while sending the message: {e}")
    finally:
        server.quit()
