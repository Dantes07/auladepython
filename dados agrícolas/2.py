import pandas as pd

dadosProdutos = pd.read_csv('dados.CSV')

indice = dadosProdutos['uso_agua'] .idxmin()
cultivo_menor_uso_H2O = dadosProdutos.loc[indice, 'tipo_cultivo']
produtividade = dadosProdutos.loc[indice, 'uso_agua']

print('Produto com a menor uso de agua:', cultivo_menor_uso_H2O , 'com', produtividade )