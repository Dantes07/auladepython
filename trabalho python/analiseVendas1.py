import pandas as pd #importando a biblioteca pandas para fazer a leitura de um arquivo csv

leiaProdutos = pd.read_csv('vendas.csv') #filtrando as informacoes do arquivo csv
print(leiaProdutos) #imprimindo a variavel com a lista vendas