import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv('dados.csv', delimiter=',')

dados.columns = dados.columns.str.strip()

print(dados.head())

produtividae_media = dados.groupby('tipo_cultivo')['produtividade'].mean()









plt.title('Preço dos Produtividade ao longo dos Anos')
plt.xlabel('ano')
plt.ylabel('tipo_cultivo')
plt.legend(title='custo_medio')

plt.grid(True)
plt.show()