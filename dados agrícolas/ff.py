import pandas as pd
import matplotlib.pyplot as plt

# Criando o DataFrame com os dados fornecidos
dados = {
    "Times": ["Santos", "Fluminense", "Vasco", "Corinthians"],
    "Masculino": [250000, 350000, 910000, 800000],
    "Feminino": [144000, 139000, 160000, 60000],
    "Ano": [2024, 2024, 2024, 2024]
}

df = pd.DataFrame(dados)

# Criando o gráfico de pizza para cada time
for index, row in df.iterrows():
    # Dados para o gráfico de pizza (salários masculinos e femininos)
    labels = ['Masculino', 'Feminino']
    sizes = [row['Masculino'], row['Feminino']]
    colors = ['#ff9999','#66b3ff']
    
    # Criando o gráfico de pizza para cada time
    plt.figure(figsize=(6,6))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    plt.title(f"Distribuição Salarial - {row['Times']} (2024)", fontsize=14)
    plt.axis('equal')  # Para deixar o gráfico de pizza circular
    plt.show()
