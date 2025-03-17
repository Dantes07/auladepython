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

# Configurando o gráfico
fig, ax = plt.subplots(figsize=(10, 6))

# Plotando os salários masculinos e femininos
df.set_index('Times')[['Masculino', 'Feminino']].plot(kind='bar', ax=ax)

# Adicionando título e rótulos aos eixos
plt.title("Comparação dos Salários de Jogadores Masculinos e Femininos (2024)", fontsize=14)
plt.xlabel("Times", fontsize=12)
plt.ylabel("Salário (em R$)", fontsize=12)

# Exibindo o gráfico
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
