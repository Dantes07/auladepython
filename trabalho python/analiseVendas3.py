import pandas as pd #importando a biblioteca pandas para fazer a leitura de um arquivo csv

dadosProdutos = pd.read_csv('vendas.CSV') #filtrando as informacoes do arquivo csv

dadosProdutos['produtos'] = dadosProdutos ['quantidade'] * dadosProdutos['preco'] 
#criando as varives para fazer a leitura do total de vendas

indice = dadosProdutos['produto'] .idxmax()
#filtrano o produto com maior indice de producao

produto_maior_produtividade = dadosProdutos.loc[indice, 'produto']
#filtrano o produto com maior indice de producao

maior_produtividade = dadosProdutos.loc[indice, 'quantidade']
#filtrano a quantidade dos indcies para o print

print('O produto com a maior produtividade foi ', produto_maior_produtividade, 'com', maior_produtividade , 'unidades')
#imprimindo as informacoes final