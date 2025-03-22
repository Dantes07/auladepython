import smtplib
import email.message

def envia_email():
    corpo_email = """
    <p>ola boa noite</p>
    <p>serguir o email </p>
    """
    msg = email.message.Message()
    msg['Subject'] = 'Python jose'
    msg['From'] = 'souzajosearmando78@gmail.com'
    msg['To'] = 'souzajosearmando78@gmail.com'
    password = 'Junior.3005'
    msg.add_header('content-Type','text/htmal')
   
    msg.set_payload(corpo_email)
    
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    
    s.login(msg['From'],password)
    s.sendmail(msg['From'],[msg['To']],msg.as_string().encode('utf-8'))
   
   
    print('email enviado')
      
envia_email()