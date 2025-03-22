import smtplib
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

df = pd.read_csv('vendas.csv')
df['TvP'] = df['quantidade'] = df['preco']
resumo_vendas = df.groupby('produto').agg({'quantidade': 'sum', 'TvP': 'sum'}).reset_index()
resumo_vendas.to_excel('relatorio.xlsx', index=False)

email_remetente = ''
email_senha = ''
email_destinatario = ''

msg = MIMEMultipart
msg['from'] = email_remetente
msg['To'] = email_destinatario
msg['subject'] = 'Relátorio de Vendas Automático'

corpo_email = '''
olá,

segue em anexo o relatório de vendas gerado automaticamente.

Atemciosamente,
Automação de vendas
'''
msg.attach(MIMEText(corpo_email, 'plain'))

anexo = open('relatorio.xlsx', 'rb')