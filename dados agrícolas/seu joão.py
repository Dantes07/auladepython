import pandas as pd
import matplotlib.pyplot as plt

dados_produtos = pd.read_csv('arquivo seu joão.csv', delimiter=',')

plt.figure(figsize=(10, 6))

for produto in dados_produtos['peixes'] .unique():

    dados_produto = dados_produtos[dados_produtos['peixes']== produto]
    plt.plot(dados_produto['ano'], dados_produto['custo_medio'], label=produto, marker='o')

plt.title('Produtividade ao longo dos Anos')
plt.xlabel('ano')
plt.ylabel('custo_medio')
plt.legend(title='Peixes')

plt.grid(True)
plt.show()