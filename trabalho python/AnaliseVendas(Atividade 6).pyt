import schedule
import time
import subprocess

def executar_analise():
    subprocess.run(['python', 'leia.py'])

schedule.every().day.at('06:45').do(executar_analise)

print('aguradando hórario programado para executar o script. . . ')

while True:
    schedule.run_pending()
    time.sleep(60)