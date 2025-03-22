import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
import matplotlib.pyplot as plt
import seaborn as sns
import schedule
import time

# Função para criar o relatório Excel
def criar_relatorio():
    # Ler o arquivo CSV
    vendas = pd.read_csv('vendas.csv')

    # Agrupar por produto e calcular a soma das vendas
    resumo_vendas = vendas.groupby('produto').agg({'quantidade': 'sum', 'valor_total': 'sum'}).reset_index()

    # Criar um Excel com duas abas: Resumo e Detalhes
    arquivo_excel = 'relatorio_vendas.xlsx'
    
    with pd.ExcelWriter(arquivo_excel, engine='openpyxl') as writer:
        resumo_vendas.to_excel(writer, sheet_name='Resumo', index=False)
        vendas.to_excel(writer, sheet_name='Detalhes', index=False)

    return arquivo_excel

# Função para gerar o gráfico de barras
def gerar_grafico():
    vendas = pd.read_csv('vendas.csv')
    quantidade_vendida = vendas.groupby('produto')['quantidade'].sum().reset_index()

    plt.figure(figsize=(10, 6))
    sns.barplot(x='produto', y='quantidade', data=quantidade_vendida, palette='viridis')

    plt.title('Quantidade Vendida por Produto', fontsize=16)
    plt.xlabel('Produto', fontsize=12)
    plt.ylabel('Quantidade Vendida', fontsize=12)

    plt.tight_layout()
    plt.savefig('grafico.png')
    plt.close()  # Fechar o gráfico

# Função para enviar o e-mail com anexo
def enviar_email(arquivo_relatorio, arquivo_grafico):
    de = "seu_email@gmail.com"
    para = "destinatario@gmail.com"
    senha = "sua_senha"

    msg = MIMEMultipart()
    msg['From'] = de
    msg['To'] = para
    msg['Subject'] = 'Relatório de Vendas'

    # Anexar o relatório Excel
    with open(arquivo_relatorio, 'rb') as file:
        anexo_relatorio = MIMEBase('application', 'octet-stream')
        anexo_relatorio.set_payload(file.read())
        encoders.encode_base64(anexo_relatorio)
        anexo_relatorio.add_header('Content-Disposition', f'attachment; filename={os.path.basename(arquivo_relatorio)}')
        msg.attach(anexo_relatorio)

    # Anexar o gráfico de barras
    with open(arquivo_grafico, 'rb') as file:
        anexo_grafico = MIMEBase('application', 'octet-stream')
        anexo_grafico.set_payload(file.read())
        encoders.encode_base64(anexo_grafico)
        anexo_grafico.add_header('Content-Disposition', f'attachment; filename={os.path.basename(arquivo_grafico)}')
        msg.attach(anexo_grafico)

    try:
        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()
        servidor.login(de, senha)
        texto = msg.as_string()
        servidor.sendmail(de, para, texto)
        servidor.quit()
        print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")

# Função principal que executa tudo
def main():
    # Passo 1: Criar o relatório
    arquivo_relatorio = criar_relatorio()

    # Passo 2: Gerar o gráfico
    gerar_grafico()

    # Passo 3: Enviar o e-mail com o relatório e gráfico anexados
    enviar_email(arquivo_relatorio, 'grafico.png')

# Agendar a execução do script para rodar todos os dias às 9h
def agendar_execucao():
    schedule.every().day.at("09:00").do(main)

    print("Tarefa agendada para rodar todos os dias às 9h.")

    while True:
        schedule.run_pending()
        time.sleep(60)

# Executar o agendamento
if __name__ == "__main__":
    agendar_execucao()