import pandas as pd

dadosProdutos = pd.read_csv('dados.CSV')

indice = dadosProdutos['tipo_cultivo'] .idxmax()
produto_maior_produtividade = dadosProdutos.loc[indice, 'tipo_cultivo']
maior_produtividade = dadosProdutos.loc[indice, 'produtividade']

print('O produto com a maior produtividade foi:', produto_maior_produtividade, 'com', maior_produtividade , 'unidades')