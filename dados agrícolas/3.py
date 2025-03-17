import pandas as pd
import matplotlib.pyplot as plt

dados_produtos = pd.read_csv('dados.csv', delimiter=',')

plt.figure(figsize=(10, 6))

for produto in dados_produtos['tipo_cultivo'] .unique():
    dados_produto = dados_produtos[dados_produtos['tipo_cultivo']== produto]
    plt.plot(dados_produto['ano'], dados_produto['custo_medio'], label=produto, marker='o')

plt.title('Preço dos Produtividade ao longo dos Anos')
plt.xlabel('ano')
plt.ylabel('tipo_cultivo')
plt.legend(title='custo_medio')

plt.grid(True)
plt.show()